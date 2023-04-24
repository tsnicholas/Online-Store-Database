"""Keeps track of the user's data by passing it into a data class."""
from collection import collection

class User(collection):
    def set_user_data(self, user : dict) -> None:
        if not self.data_exists(user):
            self.collection.insert_one(user)
        self.fname = user["first name"]
        self.lname = user["last name"]
        self.pnumber = user["phone number"]
