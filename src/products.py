"""Has a class that deals with interactions to the product collection."""
from pymongo import cursor
from pymongo.collection import Collection

class ProductStock:
    """Keeps track of the products collection and retrieves data from it."""
    def __init__(self, products : Collection):
        self.collection = products

    @staticmethod
    def convert_cursor_to_list(cursor : cursor):
        output = []
        for product in cursor:
            output.append(product)
        return output

    def get_products_in(self, category : str) -> list[dict]:
        """Retrieve products in a specified category and return it as a list of dictionaries."""
        return self.convert_cursor_to_list(self.collection.find({"category": category}))
        
    def get_products_with_id(self, id : int) -> list[dict]:
        """Retrieve products with a specific id and return it as a list of dictionaries."""
        return self.convert_cursor_to_list(self.collection.find({"id": id}))