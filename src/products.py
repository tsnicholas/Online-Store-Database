from pymongo import cursor
from pymongo.collection import Collection

class ProductStock:
    def __init__(self, products : Collection):
        self.products = products

    def getProductsIn(self, category : str) -> cursor:
        return self.products.find({"category": category})