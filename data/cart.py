"""Performs operations on the shopping cart collection of the online store database."""
from data.collection import collection

class ShoppingCart(collection):
    """Represents the cart collection of the database."""
    def get_user_cart(self, user : str) -> list[dict]:
        """Gets items from a specified user's cart."""
        return self.convert_cursor_to_list(self.collection.find({"user": user}))
    
    def delete_from_cart(self, id : int, user : str) -> None:
        """Deletes a product from the specified user's cart."""
        self.collection.delete_one({"id": id, "user": user})

    def insert_into_cart(self, user : str, productList : list[dict]) -> None:
        """Inserts a product into a user's cart."""
        for product in productList:
            insertion = product
            insertion["user"] = user
            self.collection.insert_one(insertion)
            