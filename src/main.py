import json
from user import User
from database import OnlineStore
from pymongo.collection import Collection

def getFileData(filePath):
    fileData = ""
    with open(filePath, encoding = "utf8") as file:
        fileData = json.load(file)
    return fileData

def insertData(collection : Collection, fileData : str | list):
    status = False
    if isinstance(fileData, list):
        status = collection.insert_many(fileData)
    else:
        status = collection.insert_one(fileData)
    if status:
        print(f"Successfully added data to {collection.name}.")
    else:
        print(f"Failed to insert data into {collection.name}!")

def main():
    database = OnlineStore()
    products = database.getCollection("Products")
    file_data = getFileData("../Products.json")
    insertData(products, file_data)
    users = database.getCollection("Users")
    user = User()
    if not database.dataExists(users, user.userData):
        print("Adding user...")
        insertData(users, user)
    

if __name__ == '__main__':
    main()
