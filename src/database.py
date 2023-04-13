import pymongo

class OnlineStore:
    def __init__(self):
        connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.database = connection["OnlineStore"]
