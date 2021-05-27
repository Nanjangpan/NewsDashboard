from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pymongo
from pymongo import MongoClient
# from bson import ObjectId
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
# import boto3

app = FastAPI()
url = 'mongodb://mongo-0.mongo,mongo-1.mongo,mongo-2.mongo:27017/'
client = MongoClient(url)

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

categories = {'정치': '100', '경제': '101', '사회': '102', '생활문화': '103', '세계': '104', 'IT과학': '105', '오피니언': '110', 'Hot':'200'}
@app.get("/")
async def root():
   return { "message" : "Hello World" }

# @app.exception_handler(StarletteHTTPException)
# async def custom_http_exception_handler(request, exc):
#     return RedirectResponse("/")
#에러뜰경우 root로

@app.get("/time/live")
async def time_live():
    db = client['Real_time_Result']
    cols=db.list_collection_names()     
    col_list=[]
    for i in cols:
        col_list.append(i)
    col_list.sort()
    datetime=col_list[len(col_list)-1]
    # 20201212_98
    a=int(datetime[9:])*10
    hour=(a//60)
    a=a%60
    minute=a
    return hour+"시 "+minute+"분 업데이트"


@app.get("/cate/live/")
async def cate_live(datetime: str, cate: str="Hot"):
    cate=categories[cate]
    db = client['Real_time_Result']
    cols=db.list_collection_names()     
    col_list=[]
    for i in cols:
        col_list.append(i)
    col_list.sort()
    datetime=col_list[len(col_list)-1]
    mycol = db[datetime]
    item = mycol.find_one({},{cate:1})
    result=[]
    for i in range(len(item[cate])):
        cur={}
        main_id=str(item[cate][str(i)]["id"][0])
        db=client['Info']
        main_news=db["Info"].find({"id":main_id})[0]
        cur['cluster_num']=i
        cur["img_url"]=main_news["img_url"]
        cur["title"]=main_news["title"]
        cur["url"]=main_news["url"]
        cur["press"]=main_news["press"]
        cur["keyword"]=item[cate][str(i)]["keywords"]
        cur["title_list"]=[]
        for now_id in item[cate][str(i)]["id"]:
            print(now_id)
            now_dic={}
            now_news=db["Info"].find({"id":str(now_id)})[0]
            now_dic["title"]=now_news["title"]
            now_dic["url"]=now_news["url"]
            now_dic["press"]=now_news["press"]
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

@app.get("/cate/live_nine/")
async def cate_live_nine(datetime:str,cate:str="Hot"):
    cate=categories[cate]
    db=client['Real_time_Result']
    cols=db.list_collection_names()
    col_list=[]
    for i in cols:
        col_list.append(i)
    col_list.sort()
    datetime=col_list[len(col_list)-1]
    mycol=db[datetime]
    item=mycol.find_one({},{cate:1})
    result=[]
    num=0
    for i in range(len(item[cate])):
        num=num+1
        if num==10:
            break
        cur={}
        main_id=str(item[cate][str(i)]["id"][0])
        db=client['Info']
        main_news=db["Info"].find({"id":main_id})[0]
        cur['cluster_num']=i
        cur["img_url"]=main_news["img_url"]
        cur["title"]=main_news["title"]
        cur["url"]=main_news["url"]
        cur["press"]=main_news["press"]
        cur["keyword"]=item[cate][str(i)]["keywords"]
        cur["title_list"]=[]
        for now_id in item[cate][str(i)]["id"]:
            print(now_id)
            now_dic={}
            now_news=db["Info"].find({"id":str(now_id)})[0]
            now_dic["title"]=now_news["title"]
            now_dic["url"]=now_news["url"]
            now_dic["press"]=now_news["press"]
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

@app.get("/cate/day/")
async def cate_day(datetime:str,cate:str="Hot"):
    cate=categories[cate]
    #  "2015-06-15T00:00:00+09:00"
    datetime=str(datetime)
    datetime=datetime[:3]+datetime[5:7]+datetime[8:10]
    db=client['Real_time_Result']
    mycol=db[datetime]
    item=mycol.find_one({},{cate:1})
    result=[]
    for i in range(len(item[cate])):
        cur={}
        main_id=str(item[cate][str(i)]["id"][0])
        db=client['Info']
        main_news=db["Info"].find({"id":main_id})[0]
        cur['cluster_num']=i
        cur["img_url"]=main_news["img_url"]
        cur["title"]=main_news["title"]
        cur["url"]=main_news["url"]
        cur["press"]=main_news["press"]
        cur["keyword"]=item[cate][str(i)]["keywords"]
        cur["title_list"]=[]
        for now_id in item[cate][str(i)]["id"]:
            print(now_id)
            now_dic={}
            now_news=db["Info"].find({"id":str(now_id)})[0]
            now_dic["title"]=now_news["title"]
            now_dic["url"]=now_news["url"]
            now_dic["press"]=now_news["press"]
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

@app.get("/cate/day_nine/")
async def cate_day_nine(datetime:str,cate:str="Hot"):
    cate=categories[cate]
    datetime=datetime[:3]+datetime[5:7]+datetime[8:10]
    db=client['Real_time_Result']
    mycol=db[datetime]
    item=mycol.find_one({},{cate:1})
    result=[]
    num=0
    for i in range(len(item[cate])):
        num=num+1
        if num==10:
            break
        cur={}
        main_id=str(item[cate][str(i)]["id"][0])
        db=client['Info']
        main_news=db["Info"].find({"id":main_id})[0]
        cur['cluster_num']=i
        cur["img_url"]=main_news["img_url"]
        cur["title"]=main_news["title"]
        cur["url"]=main_news["url"]
        cur["press"]=main_news["press"]
        cur["keyword"]=item[cate][str(i)]["keywords"]
        cur["title_list"]=[]
        for now_id in item[cate][str(i)]["id"]:
            print(now_id)
            now_dic={}
            now_news=db["Info"].find({"id":str(now_id)})[0]
            now_dic["title"]=now_news["title"]
            now_dic["url"]=now_news["url"]
            now_dic["press"]=now_news["press"]
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

# session = boto3.Session(profile_name='ybigta-conference')
# client = session.client('s3')
# file = './wordcloud.png'
# bucket = 'news-image'
# key = 'test.png'
# push = client.upload_file(file, bucket, key)

# session = boto3.Session(profile_name='ybigta-conference')
# client = session.client('s3')
# obj = client.get_object(Bucket='news-image', Key='config/db_config.json')
# CONFIG = json.loads(obj['Body'].read())

# @app.get("/word/live/")
# async def word_live(datetime: str):
#     return

# @app.get("/word/day/")
# async def word_live(datetime: str):
#     datetime=datetime[:3]+datetime[5:7]+datetime[8:10]
#     return  