import unittest
import mongomock
import sys
sys.path.append("../src")
from products import ProductStock
from jsonParser import JsonParser

def define_test_collection():
    client = mongomock.MongoClient("mongodb://127.0.0.1:27017/")
    testCollection = client.db.collection
    files = JsonParser.getFileData("../Products.json")
    testCollection.insert_many(files)
    return ProductStock(testCollection)

def condenseIntoList(parsed : list[dict]) -> list[str]:
    output = []
    for dic in parsed:
        output.append(dic["title"])
    return output

products = define_test_collection()

class testProducts(unittest.TestCase):
    def test_getProductsIn(self):
        expected = ["Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", "Mens Casual Premium Slim Fit T-Shirts ", "Mens Cotton Jacket", "Mens Casual Slim Fit"]
        query = products.getProductsIn("men's clothing")
        self.assertListEqual(expected, condenseIntoList(query))
    
    def test_getProductsWithId(self):
        actual = products.getProductsWithId(1)
        self.assertEqual("Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", actual[0]["title"])

if __name__ == '__main__':
    unittest.main()