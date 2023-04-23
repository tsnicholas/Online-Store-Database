"""Has a class that deals with interactions with the mongodb database."""
import pymongo
from pymongo.collection import Collection

class OnlineStore:
    """This class will deal with anything related to the database side of things."""
    def __init__(self):
        connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        self.database = connection.get_database("OnlineStore")

    def data_exists(self, collection : Collection, data : dict) -> bool:
        """Checks if the data in the dictionary already exists within the database."""
        output = False
        query = collection.find(data)
        for instance in query:
            output = True 
            for key in data:
                output = output and instance[key] == data[key]
        return output
    
    def insert_many(self, collection : Collection, files : list):
        """Inserts multiple dictionaries within the list into the collection."""
        for file in files:
            self.insert_one(collection, file)

    def insert_one(self, collection : Collection, file : str):
        """Adds a dictionary into the database if it doesn't already exist."""
        if not self.data_exists(collection, file):
            collection.insert_one(file)
