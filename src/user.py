from dataclasses import dataclass

@dataclass
class User:
    fname: str
    lname: str
    dob: str
    email: str
    pnumber: str
    
    def __init__(self, userData : dict):
        self.fname = userData["first name"]
        self.lname = userData["last name"]
        self.dob = userData["date of birth"]
        self.email = userData["email"]
        self.pnumber = userData["phone number"]
