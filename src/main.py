"""Provides the main functionality and user interaction of the project."""
from pymongo import cursor
from user import User
from database import OnlineStore
from json_parser import JsonParser
from products import ProductStock

EXIT_TERM = "exit"

def get_user_data() -> dict:
    """Prompts the user for their information and returns the answers in a dictionary."""
    user_data = {}
    data_list = ["first name", "last name", "date of birth", "email", "phone number"]
    for data in data_list:
        user_input = input(f"What's your {data}? ")
        user_data[data] = user_input
    return user_data

def main_menu(online_store : OnlineStore, products : ProductStock, user : User) -> None:
    """Serves as the main menu for the user by prompting them their options for the program."""
    user_input = ""
    while user_input != EXIT_TERM:
        user_input = input(f"What would you like to do? (Type {EXIT_TERM} to quit) ")
        match user_input:
            case "shop":
                shopping(online_store, products, user)
            case _:
                print("Not an option. Please try again.")

def shopping(online_store : OnlineStore, products : ProductStock, user : User) -> None:
    """Prompts the user for a category to select a product from and then gets their selection."""
    category = ""
    while category != EXIT_TERM:
        category = input(f"What category would you like to search? (Type {EXIT_TERM} to quit) ")
        if category != EXIT_TERM:
            product_list = convert_to_list(products.get_products_in(category), user)
            print_products(product_list)
            online_store.insert_many(online_store.database["ShoppingCart"], get_selection(product_list))

def convert_to_list(product_list : cursor, user : User) -> list[dict]:
    """Takes a cursor and converts it into a list of dictionaries."""
    output = []
    for i, product in enumerate(product_list):
        output.append(product)
        output[i]["user"] = user.pnumber
    return output

def print_products(product_list : list[dict]) -> None:
    """Prints the id and title of a product for the user."""
    for product in product_list:
        print(f"Id {product['id']}: {product['title']}")

def get_selection(product_list : list[dict]) -> list[dict]:
    """Gets the selection of products that the user wants to add to their cart."""
    selection = []
    user_selects = 0
    while user_selects != -1:
        try:    
            user_selects = int(input("Enter the index of the product you want to add to your cart (Type -1 to exit): "))
            for product in product_list:
                if product["id"] == user_selects:
                    selection.append(product)
                    break
        except TypeError:
            print("Not an integer. Please try again.")
    return selection

def main() -> None:
    """The main function that initializes everything at the beginning"""
    online_store = OnlineStore()
    products = ProductStock(online_store.database["Products"])
    try:    
        file_data = JsonParser.get_file_data("../Products.json")
        online_store.insert_many(products.collection, file_data)
    except IOError:
        print("Error: Couldn't find products.json")
    finally:
        user_data = get_user_data()
        online_store.insert_one(online_store.database["Users"], user_data)
        user = User(user_data)
        main_menu(online_store, products, user)

if __name__ == '__main__':
    main()
