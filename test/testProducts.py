"""Tests the functionality of products.py and it's class."""
import unittest
import mongomock
import sys
sys.path.append("../src")
from products import ProductStock
from json_parser import JsonParser

def define_test_collection():
    """Creates the test class for each test that's going to be ran."""
    client = mongomock.MongoClient("mongodb://127.0.0.1:27017/")
    test_collection = client.db.collection
    files = JsonParser.get_file_data("../Products.json")
    test_collection.insert_many(files)
    return ProductStock(test_collection)

def condense_into_list(parsed : list[dict]) -> list[str]:
    """Condenses a list of dictionaries into just a list of titles for testing."""
    output = []
    for dic in parsed:
        output.append(dic["title"])
    return output

products = define_test_collection()

class TestProductStock(unittest.TestCase):
    """Tests the ProductStock class."""
    def test_get_products_in(self):
        """Tests the get_products_in function."""
        expected = ["Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", "Mens Casual Premium Slim Fit T-Shirts ", "Mens Cotton Jacket", "Mens Casual Slim Fit"]
        query = products.get_products_in("men's clothing")
        self.assertListEqual(expected, condense_into_list(query))
    
    def test_get_products_with_id(self):
        """Tests the getProductsWithId function."""
        actual = products.get_products_with_id(1)
        self.assertEqual("Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", actual[0]["title"])

if __name__ == '__main__':
    unittest.main()