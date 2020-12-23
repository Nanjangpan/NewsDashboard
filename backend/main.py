from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
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

# @app.get("/test")
# async def gogo(datetime:str,cate:str="Hot"):
#     return Hot_live_Data

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