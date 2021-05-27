import redis
import logging
import subprocess
import time
from NewsCrawler.writer import Writer

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s : %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def redis_checker():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    while True:
        try:
            r.ping()
            break
        except redis.exceptions.ConnectionError as err:
            logger.error(err)
            subprocess.call("redis-server --port 6379 --daemonize yes", shell=True)

    return r


class RedisCaching():
    def __init__(self, category):
        self.rd = redis_checker()
        self.cate = str(category)
    #
    # def initialize_redis(self):
    #     # 캐싱하기 전 redis가 비어있다면 디비에서 최근 url을 꺼내와 채워준다.
    #     # 아직 적용 안함
        if self.rd.zcard(self.cate):
            pass
        else:
            latest_urls = Writer.get_latest_url(self.cate)
            for url in latest_urls[::-1]:
                self.rd.zadd(self.cate, {url[0]: f"{time.time()}"})
                time.sleep(0.005)

    def update_redis(self, url: str):
        # 새로 크롤링된 뉴스는 redis에 넣고, redis에서 장 오래된 뉴스 삭제
        old = (self.rd.zrange(self.cate, 0, 0)[0]).decode("utf-8")
        self.rd.zrem(self.cate, old)
        self.rd.zadd(self.cate, {url: f"{time.time()}"})

    def if_exist(self, url: str) -> bool:

        if self.rd.zscore(self.cate, url):
            return True
        else:
            return False

    def cache_pid(self, category, pid):
        self.rd.zadd('pid', {category: pid})
