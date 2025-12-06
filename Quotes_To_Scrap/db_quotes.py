from pymongo import MongoClient

Client = MongoClient("mongodb://localhost:27017/")

db = Client["Quotes"]

Quotes_pl_table = db["Quotes_pl_table"]
Quotes_pdp_table = db["Quotes_pdp_table"]