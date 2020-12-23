from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Item(BaseModel):
    datetime: str


todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]

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

@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
    return { "data": todos }

# @app.put("/items/{id}")
# def update_item(id: str, item: Item):
#     json_compatible_item_data = jsonable_encoder(item)
#     return JSONResponse(content=json_compatible_item_data)

@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/test")
async def gogo():
	return { "message" : "Hello World" }

@app.get("/cate/live/")
async def cate_live(datetime:str,cate:str="hot"):
    print("first_route")
    
    return

@app.get("/cate/day")
async def cate_day(datetime=str,cate:str="hot"):
    print("second_route")
    return

@app.get("/word/live")
async def word_live(cate:str,datetime=str):
    print("third_route")
    return

@app.get("/word/day")
async def word_day(cate:str,datetime=str):
    print("fourth_route")
    return
