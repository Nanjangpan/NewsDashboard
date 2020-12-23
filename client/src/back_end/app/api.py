from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
	return { "message" : "Hello World" }

# @app.post("/items/")
# async def create_item(item: Item):
# 	return item

@app.get("test/go/")
async def gogo(datetime:str="default~"):
    a="hwayoung"
    datetime=datetime+a
    return datetime

@app.get("cate/live/")
async def cate_live(datetime:str,cate:str="hot"):
    print("first_route")
    
    return

@app.get("cate/day")
async def cate_day(datetime=str,cate:str="hot"):
    print("second_route")
    return

@app.get("word/live")
async def word_live(cate:str,datetime=str):
    print("third_route")
    return

@app.get("word/day")
async def word_day(cate:str,datetime=str):
    print("fourth_route")
    return
