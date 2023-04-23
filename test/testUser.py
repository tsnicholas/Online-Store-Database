import unittest
import sys
sys.path.append("../src")
from user import User

def initializeUser() -> User:
    userData = {
            "first name": "Timothy",
            "last name": "Nicholas",
            "date of birth": "09/12/2001",
            "email": "tsnicholas@bsu.edu",
            "phone number": "(317) 993-8411"
    }
    return User(userData)

class test_User(unittest.TestCase):
    def test_init(self):
        user = initializeUser()
        self.assertEqual("Timothy", user.fname)

if __name__ == '__main__':
    unittest.main()
