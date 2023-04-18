import json
from user import User
from database import OnlineStore

class JsonParser:
    def getFileData(filePath):
        fileData = ""
        with open(filePath, encoding = "utf8") as file:
            fileData = json.load(file)
        return fileData

def main():
    onlineStore = OnlineStore()
    products = onlineStore.database.get_collection("Products")
    file_data = JsonParser.getFileData("../Products.json")
    onlineStore.insertMany(products, file_data)
    users = onlineStore.database.get_collection("Users")
    user = User()
    onlineStore.insertData(users, user.userData)

if __name__ == '__main__':
    main()
