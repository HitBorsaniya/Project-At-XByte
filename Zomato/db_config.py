from pymongo import MongoClient
Client = MongoClient('localhost', 27017)
db = Client['Zomato-Dabeli']
pl = db['pl']