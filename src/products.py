from pymongo import cursor
from pymongo.collection import Collection

class ProductStock:
    def __init__(self, products : Collection):
        self.collection = products

    def getProductsIn(self, category : str) -> cursor:
        return self.collection.find({"category": category})
    
    def getProductsWithId(self, id : int) -> cursor:
        return self.collection.find({"id": id})
    