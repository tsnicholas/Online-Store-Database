"""Performs operations on the shopping cart collection of the online store database."""
from pymongo.collection import Collection

class ShoppingCart:
    """Represents the cart collection of the database."""
    def __init__(self, cart : Collection) -> None:
        self.collection = cart

    def get_user_cart(self, user : str) -> list[dict]:
        """Gets items from a specified user's cart."""
        parsed = self.collection.find({"user": user})
        cart = []
        for product in parsed:
            cart.append(product)
        return cart
    
    def delete_from_cart(self, id : int, user : str) -> None:
        """Deletes a product from the specified user's cart."""
        self.collection.delete_one({"id": id, "user": user})

    def insert_into_cart(self, user : str, productList : list[dict]) -> None:
        """Inserts a product into a user's cart."""
        for product in productList:
            insertion = product
            insertion["user"] = user
            self.collection.insert_one(insertion)