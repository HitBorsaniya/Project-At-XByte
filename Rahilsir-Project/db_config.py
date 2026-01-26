from pymongo import MongoClient

Client = MongoClient("mongodb://localhost:27017/")
db = Client["policestation"]
collection = db["policestation"]
collection0 = db["policestation-ahmedabad"]
collection1 = db["policestation-ahmedabad-dcb"]