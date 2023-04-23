"""Tests the functionality of database.py and it's class."""
import sys
import unittest
sys.path.append("../src")
from database import OnlineStore

class TestOnlineStore(unittest.TestCase):
    """Tests the online store class."""
    def test_init(self):
        """Tests the init function of the online store class."""
        online_store = OnlineStore()
        self.assertEqual("OnlineStore", online_store.database.name)

    def test_data_exists_true_case(self):
        """Tests a true case for the data exists function."""
        online_store = OnlineStore()
        users = online_store.database.get_collection("Users")
        sample_user = {
            "first name": "Timothy",
            "last name": "Nicholas",
            "date of birth": "09/12/2001",
            "email": "tsnicholas@bsu.edu",
            "phone number": "(317) 993-8411"
        }
        users.insert_one(sample_user)
        self.assertTrue(online_store.data_exists(users, sample_user))

    def test_data_exists_false_case(self):
        """Tests a false case for the data exists function."""
        online_store = OnlineStore()
        users = online_store.database.get_collection("Users")
        fake_user = {
            "first name": "Shirou",
            "last name": "Emiya",
            "date of birth": "10/20/1985",
            "email": "semiya@bsu.edu",
            "phone number": "(666) 911-0420"
        }
        self.assertFalse(online_store.data_exists(users, fake_user))
    
if __name__ == '__main__':
    unittest.main()