from pymongo import cursor
from pymongo.collection import Collection

class ShoppingCart:
    def __init__(self, cart : Collection) -> None:
        self.collection = cart

    def get_user_cart(self, user : str) -> list[dict]:
        parsed = self.collection.find({"user": user})
        cart = []
        for product in parsed:
            cart.append(product)
        return cart
    
    def delete_from_cart(self, id : int, user : str) -> None:
        self.collection.delete_one({"id": id, "user": user})
