from pymongo import MongoClient

dbobj = MongoClient("mongodb://localhost:27017/")['teste']
