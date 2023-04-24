"""Has a class that deals with interactions with the mongodb database."""
from pymongo.collection import Collection
from pymongo import cursor

class collection:
    """This class will be inherited by the collections to initialize them and for common functions."""
    def __init__(self, collection : Collection):
        self.collection = collection

    def data_exists(self, data : dict) -> bool:
        """Checks if the data in the dictionary already exists within the database."""
        output = False
        query = self.collection.find(data)
        for instance in query:
            output = True 
            for key in data:
                output = output and instance[key] == data[key]
        return output
    
    @staticmethod
    def convert_cursor_to_list(cursor : cursor) -> list[dict]:
        output = []
        for instance in cursor:
            output.append(instance)
        return output
    