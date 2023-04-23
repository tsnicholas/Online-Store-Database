"""Tests the functionality of user.py and it's data class."""
import unittest
import sys
sys.path.append("../src")
from user import User

def initialize_user() -> User:
    """Initializes the user class for each test."""
    user_data = {
            "first name": "Timothy",
            "last name": "Nicholas",
            "date of birth": "09/12/2001",
            "email": "tsnicholas@bsu.edu",
            "phone number": "(317) 993-8411"
    }
    return User(user_data)

class TestUser(unittest.TestCase):
    """Tests the user data class"""
    def test_init(self):
        """Tests the init function of the user class."""
        user = initialize_user()
        self.assertEqual("Timothy", user.fname)

if __name__ == '__main__':
    unittest.main()
