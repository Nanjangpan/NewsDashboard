from fastapi import FastAPI
import uvicorn

from starlette.middleware.cors import CORSMiddleware

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

@app.get("/test")
<<<<<<< HEAD
<<<<<<< HEAD
async def gogo(datetime:str,cate:str="Hot"):
    return Hot_live_Data

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
async def root():
	return { "message" : "Hello World2" }

async def gogo():
    datetimes = "1234"
    cates = "ad"
    results = {"datetime" : datetimes, "cate" : cates}
    return results

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