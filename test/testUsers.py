"""Tests the functionality of user.py and it's data class."""
import unittest
import mongomock
import sys
sys.path.append("../")
from data.users import Users

def initialize_test_data() -> Users:
    client = mongomock.MongoClient("mongodb://127.0.0.1:27017/")
    test_collection = client.db.collection
    test_collection.insert_many([{"first name": "Timothy", "last name": "Nicholas", "date of birth": "09/12/2001", "email": "tsnicholas@bsu.edu", "phone number": "(317) 993-8411"},
                                 {"first name": "Billy", "last name": "Bob", "date of birth": "04/20/1973", "email": "Isuckatusingthis@Gmail.com", "phone number": "(317) 856-2377"}])
    return Users(test_collection)

def delete_randomized_id(parsed : list[dict]) -> list[dict]:
    output = []
    for dic in parsed:
        del dic["_id"]
        output.append(dic)
    return output

class TestUser(unittest.TestCase):
    """Tests the user data class"""
    def test_init(self):
        user = initialize_test_data()
        expected = [{"first name": "Timothy", "last name": "Nicholas", "date of birth": "09/12/2001", "email": "tsnicholas@bsu.edu", "phone number": "(317) 993-8411"},
                    {"first name": "Billy", "last name": "Bob", "date of birth": "04/20/1973", "email": "Isuckatusingthis@Gmail.com", "phone number": "(317) 856-2377"}]
        self.assertListEqual(expected, delete_randomized_id(user.collection.find()))
    
    def test_set_user_data_existing_case(self):
        user = initialize_test_data()
        expected = [{"first name": "Timothy", "last name": "Nicholas", "date of birth": "09/12/2001", "email": "tsnicholas@bsu.edu", "phone number": "(317) 993-8411"},
                    {"first name": "Billy", "last name": "Bob", "date of birth": "04/20/1973", "email": "Isuckatusingthis@Gmail.com", "phone number": "(317) 856-2377"}]
        user.insert_user({"first name": "Timothy", "last name": "Nicholas", "date of birth": "09/12/2001", "email": "tsnicholas@bsu.edu", "phone number": "(317) 993-8411"})
        self.assertListEqual(expected, delete_randomized_id(user.collection.find()))

    def test_set_user_data_new_case(self):
        user = initialize_test_data()
        expected = [{"first name": "Timothy", "last name": "Nicholas", "date of birth": "09/12/2001", "email": "tsnicholas@bsu.edu", "phone number": "(317) 993-8411"},
                    {"first name": "Billy", "last name": "Bob", "date of birth": "04/20/1973", "email": "Isuckatusingthis@Gmail.com", "phone number": "(317) 856-2377"},
                    {"first name": "Vienna", "last name": "Nicholas", "date of birth": "01/06/2003", "email": "goblingirl@Gmail.com", "phone number": "(317) 993-8422"}]
        user.insert_user({"first name": "Vienna", "last name": "Nicholas", "date of birth": "01/06/2003", "email": "goblingirl@Gmail.com", "phone number": "(317) 993-8422"})
        self.assertListEqual(expected, delete_randomized_id(user.collection.find()))

if __name__ == '__main__':
    unittest.main()
