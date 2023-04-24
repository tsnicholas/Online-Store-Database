"""Tests the functionality of database.py and it's class."""
import sys
import unittest
import mongomock
sys.path.append("../")
from data.collection import collection

class TestCollection(unittest.TestCase):
    """Tests the collection class."""
    sample_user = {
            "first name": "Timothy",
            "last name": "Nicholas",
            "date of birth": "09/12/2001",
            "email": "tsnicholas@bsu.edu",
            "phone number": "(317) 993-8411"
    }
    
    def test_data_exists_true_case(self):
        """Tests a true case for the data exists function."""    
        test_collection = mongomock.MongoClient("mongodb://127.0.0.1:27017/").db.collection
        test_collection.insert_one(self.sample_user)
        test = collection(test_collection)
        self.assertTrue(test.data_exists(self.sample_user))

    def test_data_exists_false_case(self):
        """Tests a false case for the data exists function."""
        fake_user = {
            "first name": "Shirou",
            "last name": "Emiya",
            "date of birth": "10/20/1985",
            "email": "tsnicholas@bsu.edu",
            "phone number": "(666) 911-0420"
        }
        test_collection = mongomock.MongoClient("mongodb://127.0.0.1:27017/").db.collection
        test_collection.insert_one(self.sample_user)
        test = collection(test_collection)
        self.assertFalse(test.data_exists(fake_user))
    
if __name__ == '__main__':
    unittest.main()