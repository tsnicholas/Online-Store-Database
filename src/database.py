import pymongo
from pymongo.collection import Collection

class OnlineStore:
    def __init__(self):
        connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.database = connection.get_database("OnlineStore")
    
    def dataExists(self, collection : Collection, data : dict) -> bool:
        output = False
        query = collection.find(data)
        for instance in query:
            output = True 
            for key in data:
                output = output and instance[key] == data[key]
        return output
    