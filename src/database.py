import pymongo
from pymongo.collection import Collection

class OnlineStore:
    def __init__(self):
        connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.database = connection["OnlineStore"]

    def getCollection(self, collection) -> Collection:
        return self.database[collection]
    
    def dataExists(self, collection : Collection, data) -> bool:
        query = collection.find(data)
        