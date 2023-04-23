from pymongo import cursor
from user import User
from database import OnlineStore
from jsonParser import JsonParser
from products import ProductStock

EXIT_TERM = "exit"

def getUserData() -> dict:
    userData = {}
    dataList = ["first name", "last name", "date of birth", "email", "phone number"]
    for data in dataList:
        userInput = input(f"What's your {data}? ")
        userData[data] = userInput
    return userData

def mainmenu(onlineStore : OnlineStore, products : ProductStock, user : User) -> None:
    userInput = ""
    while userInput != EXIT_TERM:
        userInput = input(f"What would you like to do? (Type {EXIT_TERM} to quit) ")
        match userInput:
            case "shop":
                shopping(onlineStore, products, user)
            case _:
                print("Not an option. Please try again.")

def shopping(onlineStore : OnlineStore, products : ProductStock, user : User) -> None:
    category = ""
    while category != EXIT_TERM:
        category = input(f"What category would you like to search? (Type {EXIT_TERM} to quit) ")
        if category != EXIT_TERM:
            productList = convertToList(products.getProductsIn(category), user)
            printProducts(productList)
            onlineStore.insertMany(onlineStore.database["ShoppingCart"], getSelection(productList))

def convertToList(productList : cursor, user : User) -> list[dict]:
    list = []
    for i, product in enumerate(productList):
        list.append(product)
        list[i]["user"] = user.pnumber
    return list

def printProducts(productList : list[dict]) -> None:
    for product in productList:
        print(f"Id {product['id']}: {product['title']}")

def getSelection(productList : list[dict]) -> list[dict]:
    selection = []
    userSelects = 0
    while userSelects != -1:
        try:    
            userSelects = int(input("Enter the index of the product you want to add to your cart (Type -1 to exit): "))
            for product in productList:
                if product["id"] == userSelects:
                    selection.append(product)
                    break
        except TypeError:
            print("Not an integer. Please try again.")
    return selection

def main() -> None:
    onlineStore = OnlineStore()
    products = ProductStock(onlineStore.database["Products"])
    try:    
        file_data = JsonParser.getFileData("../Products.json")
    except IOError:
        print("Error: Couldn't find products.json")
    finally:
        onlineStore.insertMany(products.collection, file_data)
        userData = getUserData()
        onlineStore.insertOne(onlineStore.database["Users"], userData)
        user = User(userData)
        mainmenu(onlineStore, products, user)

if __name__ == '__main__':
    main()
