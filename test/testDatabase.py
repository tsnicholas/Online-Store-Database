import unittest
import mongomock
import sys
sys.path.append("../src")
from database import OnlineStore

class testOnlineStore(unittest.TestCase):
    def test_init(self):
        onlineStore = OnlineStore()
        expected = mongomock.MongoClient().get_database("OnlineStore").name
        self.assertEqual(expected, onlineStore.database.name)

    def test_dataExists_TrueCase(self):
        onlineStore = OnlineStore()
        users = onlineStore.database.get_collection("Users")
        sampleUser = {
            "first name": "Timothy",
            "last name": "Nicholas",
            "date of birth": "09/12/2001",
            "email": "tsnicholas@bsu.edu",
            "phone number": "(317) 993-8411"
        }
        users.insert_one(sampleUser)
        self.assertTrue(onlineStore.dataExists(users, sampleUser))

    def test_dataExists_FalseCase(self):
        onlineStore = OnlineStore()
        users = onlineStore.database.get_collection("Users")
        fakeUser = {
            "first name": "Shirou",
            "last name": "Emiya",
            "date of birth": "10/20/1985",
            "email": "semiya@bsu.edu",
            "phone number": "(666) 911-0420"
        }
        self.assertFalse(onlineStore.dataExists(users, fakeUser))
    
if __name__ == '__main__':
    unittest.main()