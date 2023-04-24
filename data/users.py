"""Keeps track of the user's data by passing it into a data class."""
from data.collection import collection

class Users(collection):
    def insert_user(self, user : dict) -> None:
        if not self.data_exists(user):
            self.collection.insert_one(user)
