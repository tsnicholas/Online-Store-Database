import unittest
import mongomock
import sys
from pymongo import cursor
sys.path.append("../src")
from cart import ShoppingCart

def initialize_test_data() -> ShoppingCart:
    client = mongomock.MongoClient("mongodb://127.0.0.1:27017/")
    test_collection = client.db.collection
    test_collection.insert_many([{"id": 1, "title": "Breath of the Wild", "user": "(317) 993-8411"}, 
                                 {"id": 2, "title": "Skinny Jeans", "user": "(317) 856-2377"},
                                 {"id": 3, "title": "Rick and Morty Box Set", "user": "(317) 518-1936"}, 
                                 {"id": 3, "title": "Rick and Morty Box Set", "user": "(317) 993-8411"}])
    return ShoppingCart(test_collection)

def delete_randomized_id(parsed : list[dict]) -> list[dict]:
    output = []
    for dic in parsed:
        del dic["_id"]
        output.append(dic)
    return output

class TestShoppingCart(unittest.TestCase):
    def test_init(self):
        cart = initialize_test_data()
        expected = [{"id": 1, "title": "Breath of the Wild", "user": "(317) 993-8411"}, 
                    {"id": 2, "title": "Skinny Jeans", "user": "(317) 856-2377"},
                    {"id": 3, "title": "Rick and Morty Box Set", "user": "(317) 518-1936"}, 
                    {"id": 3, "title": "Rick and Morty Box Set", "user": "(317) 993-8411"}]
        self.assertListEqual(expected, delete_randomized_id(cart.collection.find()))
    
    def test_get_user_cart(self):
        cart = initialize_test_data()
        expected = [{"id": 1, "title": "Breath of the Wild", "user": "(317) 993-8411"},
                    {"id": 3, "title": "Rick and Morty Box Set", "user": "(317) 993-8411"}]
        self.assertListEqual(expected, delete_randomized_id(cart.get_user_cart("(317) 993-8411")))

    def test_delete_from_cart(self):
        cart = initialize_test_data()
        expected = [{"id": 1, "title": "Breath of the Wild", "user": "(317) 993-8411"}]
        cart.delete_from_cart(3, "(317) 993-8411")
        self.assertListEqual(expected, delete_randomized_id(cart.collection.find({"user": "(317) 993-8411"})))

    def test_insert_into_cart_one_case(self):
        cart = initialize_test_data()
        expected = [{"id": 2, "title": "Skinny Jeans", "user": "(317) 856-2377"}, 
                    {"id": 4, "title": "Almond Milk", "user": "(317) 856-2377"}]
        cart.insert_into_cart("(317) 856-2377", [{"id": 4, "title": "Almond Milk"}])
        self.assertListEqual(expected, delete_randomized_id(cart.collection.find({"user": "(317) 856-2377"})))

    def test_insert_into_cart_many_case(self):
        cart = initialize_test_data()
        expected = [{"id": 2, "title": "Skinny Jeans", "user": "(317) 856-2377"},
                    {"id": 3, "title": "Rick and Morty Box Set", "user": "(317) 856-2377"},
                    {"id": 4, "title": "Almond Milk", "user": "(317) 856-2377"}]
        cart.insert_into_cart("(317) 856-2377", [{"id": 3, "title": "Rick and Morty Box Set"}, {"id": 4, "title": "Almond Milk"}])
        self.assertListEqual(expected, delete_randomized_id(cart.collection.find({"user": "(317) 856-2377"})))

if __name__ == '__main__':
    unittest.main()