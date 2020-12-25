from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from pymongo import MongoClient

from bson import ObjectId
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


Hot_live_Data = [
    {
        'cluster_num' : 1,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 2,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "2_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],        
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA",
                'show' : 'True'
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 3,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "3_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 4,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 5,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 6,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 7,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 8,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 9,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'True',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 10,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'wait',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    },
    {
        'cluster_num' : 11,
        'image_url': "https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-19/s320x320/68928347_372170763455402_1476590304457916416_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_ohc=4qrCUJ1JsxAAX-YEYU1&tp=1&oh=bf11422bdd01df68152b248c41aafaf4&oe=600E61FC",
        'title': "1_'머리 때리고 코 비틀고' 어린이집 원생 7명 학대...20대 교사 입건",
        'url': "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529635&rankingType=RANKING",
        'press': "YTN",
        'keyword': ["이시은", "바보", "멍청이"],
        'show' : 'wait',
        'title_list': [
            {
                'title' : "명동 네이`처리퍼블릭 공시가격 3.8% 오르는데 보유세는 26.8%↑(종합)",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=001&aid=0012098013",
                'press' : "YBIGTA"
            },{
                'title' : "잠시 뒤 정경심 1심 선고...법원 결론은?",
                'url' : "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=052&aid=0001529633",
                'press' : "YBIGTA"
            },{
                'title' : "나경원, 결국 아들 출생증명서 공개 '뭘 보여줘도 못 믿겠지만'",
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529583&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },{
                'title' : '신규 환자 다시 1,092명..."오늘부터 영국행 항공기 운항 중단"',
                'url' : "https://news.naver.com/main/ranking/read.nhn?mode=LSD&mid=shm&sid1=001&oid=052&aid=0001529591&rankingType=RANKING",
                'press' : "YBIGTA"
            },
        ], 
    }   
]


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["Content-Type", "application/xml"],
)

@app.get("/")
async def root():
   return { "message" : "Hello World" }

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    return RedirectResponse("/")
#에러뜰경우 root로

@app.get("/tests")
async def gogos(datetime:str,cate:str="Hot"):
    return Hot_live_Data

@app.get("/test")
async def gogo(datetime:str,cate:str="Hot",deleteItem:str=False):
    result=[]
    if(deleteItem=="False"):
        a=0
        for i in Hot_live_Data:
            if i['show']!='False':
                result.append(i)
            if a==9:
                break
        return result
    else:
        num=int(deleteItem)
        Hot_live_Data[num-1]['show']='False'
        a=0
        for i in Hot_live_Data:
            if i['show']!='False':
                result.append(i)
                a+=1
            if a==9:
                break
        return result

# @app.get("cate/live/")
# async def cate_live(datetime:str,cate:str="hot"):
#     print("first_route")
    
#     return

# @app.get("cate/day")
# async def cate_day(datetime=str,cate:str="hot"):
#     print("second_route")
#     return

# @app.get("word/live")
# async def word_live(cate:str,datetime=str):
#     print("third_route")
#     return

# @app.get("word/day")
# async def word_day(cate:str,datetime=str):
#     print("fourth_route")
#     return



client = MongoClient('localhost', 27017)
#host,port
db = client.dbname
print('MongoDB Connected.')

@app.on_event("startup")
async def startup_db_client():
    client = MongoClient('localhost', 27017)
    #host,port
    db = client.dbname
    print('MongoDB Connected.')

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
    print('MongoDB Closed.')

# class User(BaseModel):
#     _id: ObjectId
#     name: str
#     email: str
#     username: str


# @app.on_event("startup")
# async def startup_db_client():
#     app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
#     app.mongodb = app.mongodb_client[settings.DB_NAME]


# @app.on_event("shutdown")
# async def shutdown_db_client():
#     app.mongodb_client.close()


# app.include_router(todo_router, tags=["tasks"], prefix="/task")

if __name__ == "__main__":
    uvicorn.run(
        "main.app", 
        host="localhost", 
        port=8000, 
        reload=True)