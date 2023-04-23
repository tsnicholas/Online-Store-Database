"""Keeps track of the user's data by passing it into a data class."""
from dataclasses import dataclass

@dataclass
class User:
    """A data class that keeps track of the user's information."""
    fname: str
    lname: str
    dob: str
    email: str
    pnumber: str
    
    def __init__(self, user_data : dict):
        self.fname = user_data["first name"]
        self.lname = user_data["last name"]
        self.dob = user_data["date of birth"]
        self.email = user_data["email"]
        self.pnumber = user_data["phone number"]
