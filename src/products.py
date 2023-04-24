"""Has a class that deals with interactions to the product collection."""
from collection import collection

class ProductStock(collection):
    """Keeps track of the products collection and retrieves data from it."""
    def get_products_in(self, category : str) -> list[dict]:
        """Retrieve products in a specified category and return it as a list of dictionaries."""
        return self.convert_cursor_to_list(self.collection.find({"category": category}))
        
    def get_products_with_id(self, id : int) -> list[dict]:
        """Retrieve products with a specific id and return it as a list of dictionaries."""
        return self.convert_cursor_to_list(self.collection.find({"id": id}))
    
    def insert_products(self, products : list[dict]) -> None:
        """Inserts each product into the database under the product collection."""
        for product in products:
            if not self.data_exists(product):
                self.collection.insert_one(product)

    