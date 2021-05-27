import pymongo
from pymongo import MongoClient
from datetime import datetime


client=MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())
db=client["hi"]
mycol=db["1"]
mycol.insert_one({"asd":{"asd":"qwe"}})
mycol=db["2"]
mycol.insert_one({"asd":{"asd":"qwe"}})
mycol=db["3"]
mycol.insert_one({"asd":{"asd":"qwe"}})
mycol=db["4"]
mycol.insert_one({"asd":{"asd":"qwe"}})

cols=db.list_collection_names()
col_list=[]
for i in cols:
    col_list.append(i)
col_list.sort()
datetime=col_list[len(col_list)-1]
print(datetime)
# def set_date():
#     # mongodb에 들어갈 날짜 형식 ex.20201111_1
#     today = datetime.today()
#     n = (today.hour * 60 + today.minute) // 10
#     date_key = f"{today.year}{today.month}{today.day}_{n}"
#     return date_key

# def live_model(result):
#     date=str(set_date())
#     db = client['Real_time_Result']
#     mycol = db[date]
#     mycol.insert_one(result)

# def day_model(date,result):
#     db = client['Day_Result']
#     mycol = db[date]
#     mycol.insert_one(result)