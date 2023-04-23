"""Has a class that deals with interactions to the product collection."""
from pymongo import cursor
from pymongo.collection import Collection

class ProductStock:
    """Keeps track of the products collection and retrieves data from it."""
    def __init__(self, products : Collection):
        self.collection = products

    def get_products_in(self, category : str) -> cursor:
        """Retrieve products in a specified category."""
        return self.collection.find({"category": category})
    
    def get_products_with_id(self, id : int) -> cursor:
        """Retrieve products with a specific id."""
        return self.collection.find({"id": id})
    