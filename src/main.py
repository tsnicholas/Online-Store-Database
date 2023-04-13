import json
from database import OnlineStore

def getFileData():
    file_data = None
    with open("../Products.json", encoding="utf8") as json_file:
        file_data = json.load(json_file)
    return file_data

def main():
    store = OnlineStore()
    products = store.database["Products"]
    file_data = getFileData()
    if isinstance(file_data, list):
        products.insert_many(file_data)
    else:
        products.insert_one(file_data)

if __name__ == '__main__':
    main()
