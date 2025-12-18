from pymongo import MongoClient
Client = MongoClient('localhost', 27017)
db = Client['Amazon-Variation-Project']


pl = db['pl']