from pymongo import MongoClient

Client = MongoClient('mongodb://localhost:27017/')

db = Client['hindware']
cate = db['cate']

pl = db['pl']