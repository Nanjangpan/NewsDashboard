from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pymongo
from pymongo import MongoClient
from bson import ObjectId
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException


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
    # deleteItem은 cluster_num, 해당 cluster_num의 show값을 'False'로 변경 후
    # show값이 'False'가 아닌 9개의 데이터 반환


@app.get("/cate/live/")
async def cate_live(datetime:str,cate:str="hot"):
    print("first_route")
    result=[]
    item=Real_time_Result.datetime.find({},{cate:true})
    a=list(item[cate].keys())
    a.sort()
    for i in a:
        cur={}
        main_id=item[cate][i]["id_list"][0]
        main_news=Info.Info.find({},{main_id:true})
        cur['cluster_num']=i
        cur["image_url"]=main_news[main_id]["image_url"]
        cur["title"]=main_news[main_id]["title"]
        cur["url"]=main_news[main_id]["url"]
        cur["press"]=main_news[main_id]["press"]
        cur["keyword_list"]=item[cate][i]["id_list"]
        cur["show"]='wait'
        cur["title_list"]=[]
        for now_id in item[cate][i]["id_list"]:
            now_dic={}
            now_news=Info.Info.find({},{now_id:true})
            now_dic["title"].append(now_news[now_id]["title"])
            now_dic["url"].append(now_news[now_id]["url"])
            now_dic["press"].append(now_news[now_id]["press"])
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

@app.get("/cate/day/")
async def cate_live(datetime:str,cate:str="hot"):
    print("second_route")
    result=[]
    item=Day_Result.day.find({},{cate:true})
    a=list(item[cate].keys())
    a.sort()
    for i in a:
        cur={}
        main_id=item[cate][i]["id_list"][0]
        main_news=Info.Info.find({},{main_id:true})
        cur['cluster_num']=i
        cur["image_url"]=main_news[main_id]["image_url"]
        cur["title"]=main_news[main_id]["title"]
        cur["url"]=main_news[main_id]["url"]
        cur["press"]=main_news[main_id]["press"]
        cur["keyword_list"]=item[cate][i]["id_list"]
        cur["show"]='wait'
        cur["title_list"]=[]
        for now_id in item[cate][i]["id_list"]:
            now_dic={}
            now_news=Info.Info.find({},{now_id:true})
            now_dic["title"].append(now_news[now_id]["title"])
            now_dic["url"].append(now_news[now_id]["url"])
            now_dic["press"].append(now_news[now_id]["press"])
            cur["title_list"].append(now_dic)
        result.append(cur)
    return result

if __name__ == "__main__":
    uvicorn.run(
        "main.app", 
        host="localhost", 
        port=8000, 
        reload=True)

# class front_in(BaseModel):
#     datetime: str
#     cate: str

# class front_out(BaseModel):
#     cluster_num: int
#     image_url: str
#     title: str
#     url: str
#     press: str
#     keyword: list[str]
#     title_list: list[dict(str, str, str)]