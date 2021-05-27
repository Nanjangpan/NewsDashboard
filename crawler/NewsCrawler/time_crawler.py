from time import sleep
from bs4 import BeautifulSoup
from multiprocessing import Process
import os
import requests
import re
from datetime import datetime
from typing import List, Dict
import logging
from NewsCrawler.category import categories
from NewsCrawler.exceptions import *
from NewsCrawler.articleparser import ArticleParser
from NewsCrawler.writer import Writer
from NewsCrawler.redis_caching import RedisCaching

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s : %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Crawler(object):
    """실시간 크롤러"""

    def __init__(self, category_input: str):
        self.category_name: str = category_input
        self.category: int = categories[self.category_name]
        self.date = {'start_month': 0, 'start_day': 0, 'end_month': 0, 'end_day': 0}
        self.headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)\
                                        # AppleWebKit/537.36 (KHTML, like Gecko)\
                                         Chrome/63.0.3239.132 Safari/537.36',
                        "Accept": "text/html",
                        "Pragma": "no-cache",
                        "Cache-Control": "no-cache"}
        self.caching = RedisCaching(self.category)

    def get_url_data(self, url: str, max_tries=10):
        """카테고리별 뉴스 페이지 request.get"""
        remaining_tries = int(max_tries)

        while remaining_tries > 0:
            try:
                return requests.get(url, headers=self.headers)
            except requests.exceptions:
                sleep(60)
            remaining_tries = remaining_tries - 1
        raise ResponseTimeout()

    def get_url_target(self) -> List[str]:
        """카테고리별 뉴스 페이지에서 메인으로 보이는 20개의 뉴스 기사만 뽑아서 기
        redis에 없는 것만 골라내기"""
        # Multi Process PID
        pid = str(os.getpid())
        logger.info(f"{datetime.now()}, {self.category_name} PID: {pid}")
        self.caching.cache_pid(category_name, pid)

        URL = "http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=" + str(
            self.category)
        request = self.get_url_data(URL)
        document = BeautifulSoup(request.content, 'html.parser')
        # html - newsflash_body - type06_headline, type06
        # 각 페이지에 있는 기사들 가져오기
        post_temp = document.select('.newsflash_body .type06_headline li dl')
        post_temp.extend(document.select('.newsflash_body .type06 li dl'))  # 20개

        target_urls = []
        # 각 페이지에 있는 기사들의 url 저장
        for line in post_temp:
            # https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=100&oid=056&aid=0010424247 이런애들
            _url = line.a.get('href')  # 해당되는 page에서 모든 기사들의 URL을 post 리스트에 넣음
            if self.caching.if_exist(_url):
                continue
            else:
                target_urls.append(_url)
        del post_temp

        return target_urls

    def news_crawling(self, urls: List[str]):
        now = str(datetime.now())
        news_data = []
        urls = urls[::-1]  # 오래된 기사부터 먼저 캐싱하기 위해 순서 reverse

        for url in urls:

            news_id = url.split('&')[-1].split('=')[1]  # 고유번호
            # 기사 HTML 가져옴
            request_content = self.get_url_data(url)
            try:
                document_content = BeautifulSoup(request_content.content, 'html.parser')
            except Exception as e:
                logger.error(f"crawling failed for url:{url}, Error: {e}")
                continue

            self.caching.update_redis(url)
            try:
                # 기사 제목 가져옴
                tag_headline = document_content.find_all('h3', {'id': 'articleTitle'}, {'class': 'tts_head'})
                text_headline = ''  # 뉴스 기사 제목 초기화
                # 기사  제목 예시 : [<h3 id="articleTitle">]제목내용</h3>]
                # 필요 없는 내용 날리고 깔끔하게 처리해주기
                text_headline = text_headline + ArticleParser.clear_headline(
                    str(tag_headline[0].find_all(text=True)))
                if not text_headline:  # 공백일 경우 기사 제외 처리
                    continue

                # 기사 본문 가져옴
                tag_content = document_content.find_all('div', {'id': 'articleBodyContents'})
                text_sentence = ''  # 뉴스 기사 본문 초기화
                text_sentence = text_sentence + ArticleParser.clear_content(str(tag_content[0].find_all(text=True)))
                if not text_sentence:  # 공백일 경우 기사 제외 처리
                    continue

                # 기사 언론사 가져옴(공백 허용)
                tag_company = document_content.find_all('meta', {'property': 'me2:category1'})
                text_company = ''  # 언론사 초기화
                text_company = text_company + str(tag_company[0].get('content'))

                # 기사 작성 날짜
                tag_date = document_content.find_all('span', {'class': 't11'})
                text_date = ''
                text_date = text_date + str(tag_date[0].find_all(text=True)[0])
                if not text_date:
                    continue

                # ima Url ( if exists )
                tag_img = document_content.find_all('span', {'class': 'end_photo_org'})
                text_imgurl = ''
                text_imgurl_lst = re.findall('https?://(?:[-\w./]|(?:%[\da-fA-F]))+', str(tag_img))
                if text_imgurl_lst:
                    text_imgurl = text_imgurl_lst[0]

                info = {'category': self.category, 'id': news_id, 'title': text_headline, 'url': url, \
                        'img_url': text_imgurl, 'datetime': now, 'press': text_company, 'content': text_sentence}
                news_data.append(info)

                del text_company, text_sentence, text_headline
                del tag_company
                del tag_content, tag_headline
                del request_content, document_content
                del text_imgurl_lst

            except Exception as e:
                logger.error(f"{e}, Parsing {category_name} PID: {str(os.getpid())} Date: {now} Is FAILED.")
                continue

        writer = Writer.insert_values_to_db('news_info', news_data)
        if writer == 'Done':
            logger.info(
                f"Insert: {category_name} PID: {str(os.getpid())} {[x['id'] for x in news_data]} articles in DataBase")
        else:
            logger.error(f"inserting {news_data} Failed.")
        del news_data

    def continuous_crawling(self):
        while True:
            now_urls = self.get_url_target()
            if not now_urls:
                sleep(30)
                continue
            else:
                self.news_crawling(now_urls)
                print(len(now_urls))
                sleep(30)


def set_date():
    # mongodb에 들어갈 날짜 형식 ex.20201111_1
    today = datetime.today()
    n = (today.hour * 60 + today.minute) // 10
    date_key = f"{today.year}{today.month}{today.day}_{n}"
    return date_key


if __name__ == "__main__":
    categories = {'정치': 100, '경제': 101, '사회': 102, '생활문화': 103, '세계': 104, 'IT과학': 105, '오피니언': 110}
    keys = list(categories.keys())
    procs = []
    for category_name in keys:
        crawler = Crawler(category_name)
        proc = Process(target=crawler.continuous_crawling)
        procs.append(proc)
        proc.start()
        sleep(3)

    for proc in procs:
        proc.join()
