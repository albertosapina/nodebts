from pymongo import MongoClient
from nosql_wiki.settings import MONGO_SETTINGS

def getDatabase():
    client = MongoClient(MONGO_SETTINGS["connection_string"])
    db = client[MONGO_SETTINGS["db_name"]]
    return db