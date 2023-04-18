import unittest
import mongomock
import sys
sys.path.append("../src")
from products import ProductStock
from main import JsonParser

class testProducts(unittest.TestCase):
    def test_getProductsIn(self):
        client = mongomock.MongoClient("mongodb://127.0.0.1:27017/")
        testCollection = client.db.collection
        files = JsonParser.getFileData("../Products.json")
        testCollection.insert_many(files)
        products = ProductStock(testCollection)
        expected = ["Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops", "Mens Casual Premium Slim Fit T-Shirts ", "Mens Cotton Jacket", "Mens Casual Slim Fit"]
        query = products.getProductsIn("men's clothing")
        self.assertListEqual(expected, self.condenseIntoList(query))
    
    def condenseIntoList(self, parsed : list[dict]) -> list[str]:
        output = []
        for dic in parsed:
            output.append(dic["title"])
        return output

if __name__ == '__main__':
    unittest.main()