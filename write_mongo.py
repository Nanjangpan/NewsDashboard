import pymongo
from pymongo import MongoClient
from datetime import datetime

url = 'mongodb://mongo-0.mongo,mongo-1.mongo,mongo-2.mongo:27017'
client=MongoClient(url)
def set_date():
    # mongodb에 들어갈 날짜 형식 ex.20201111_1
    today = datetime.today()
    n = (today.hour * 60 + today.minute) // 10
    date_key = f"{today.year}{today.month}{today.day}_{n}"
    return date_key

def live_model(result):
    date=str(set_date())
    db = client['Real_time_Result']
    mycol = db[date]
    mycol.insert_one(result)

def day_model(date,result):
    db = client['Day_Result']
    mycol = db[date]
    mycol.insert_one(result)