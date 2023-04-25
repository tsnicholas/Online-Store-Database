"""Provides the main functionality and user interaction of the project."""
import pymongo
from data.users import Users
from data.json_parser import JsonParser
from data.products import ProductStock
from data.cart import ShoppingCart

EXIT_TERM = -1
USER_DATA = {}
DATA_LIST = ["first name", "last name", "date of birth", "email", "phone number"]
PNUMBER = 4

def get_user_data() -> None:
    """Prompts the user for their information and returns the answers in a dictionary."""
    for data in DATA_LIST:
        USER_DATA[data] = input(f"What's your {data}? ")

def main_menu(cart : ShoppingCart, products : ProductStock) -> None:
    """Serves as the main menu for the user by prompting them their options for the program."""
    user_input = 0
    while user_input != EXIT_TERM:
        try:
            user_input = int(input("What would you like to do?\n1. Shop for products.\n2. View your order summary.\n3. Delete from your cart.\n"
                                   f"(Type {EXIT_TERM} to quit) "))
            match user_input:
                case -1:
                    break
                case 1:
                    shopping(cart, products)
                case 2:
                    order_summary(cart)
                case 3:
                    delete_from_cart(cart)
                case _:
                    print("Not an option. Please try again.")
        except TypeError:
            print("Not an integer. Please try again.")

def shopping(cart : ShoppingCart, products : ProductStock) -> None:
    """Prompts the user for a category to select a product from and then gets their selection."""
    category = ""
    while True:
        category = input(f"What category would you like to search? (Type {EXIT_TERM} to quit) ")
        if category == str(EXIT_TERM):
            break
        product_list = products.get_products_in(category)
        print_products(product_list)
        cart.insert_into_cart(USER_DATA[DATA_LIST[PNUMBER]], get_selection(product_list))

def print_products(product_list : list[dict]) -> None:
    """Prints the id and title of a product for the user."""
    for product in product_list:
        print(f"Id {product['id']}: {product['title']}")

def get_selection(product_list : list[dict]) -> list[dict]:
    """Gets the selection of products that the user wants to add to their cart."""
    selection = []
    user_selects = 0
    while user_selects != EXIT_TERM:
        try:    
            user_selects = int(input(f"Enter the index of the product you want to add to your cart (Type {EXIT_TERM} to quit): "))
            exists = False
            for product in product_list:
                if product["id"] == user_selects:
                    selection.append(product)
                    exists = True
                    break
            if not exists:
                print("That product isn't in this category or doesn't exist. Please try again.")
        except TypeError:
            print("Not an integer. Please try again.")
    return selection

def order_summary(cart : ShoppingCart) -> None:
    """Displays all the products within the user's cart."""
    user_cart = cart.get_user_cart(USER_DATA[DATA_LIST[PNUMBER]])
    print(f"{USER_DATA[DATA_LIST[0]]} {USER_DATA[DATA_LIST[1]]}'s cart: ")
    for product in user_cart:
        print(f"id: {product['id']}, title: {product['title']}, category: {product['category']}, price: {product['price']}, rating: {product['rating']['rate']}.")

def delete_from_cart(cart : ShoppingCart) -> None:
    """Deletes products from the user's cart."""
    while True:    
        try:
            product_id = int(input(f"What's the id of the product you'd like to delete? (Type {EXIT_TERM} to quit) "))
            if product_id == EXIT_TERM:
                break
            cart.delete_from_cart(product_id, USER_DATA[DATA_LIST[PNUMBER]])
            print("Successfully deleted from cart.")
        except TypeError:
            print("Not an integer. Please try again.")

def main() -> None:
    """The main function that initializes everything at the beginning."""
    database = pymongo.MongoClient("mongodb://127.0.0.1:27017/")["OnlineStore"]
    products = ProductStock(database["Products"])
    users = Users(database["Users"])
    cart = ShoppingCart(database["ShoppingCart"])
    try:    
        file_data = JsonParser.get_file_data("Products.json")
        products.insert_products(file_data)
    except IOError:
        print("Warning: Couldn't find products.json. Products collection may be empty going forward.")
    finally:
        get_user_data()
        users.insert_user(USER_DATA)
        main_menu(cart, products)

if __name__ == '__main__':
    main()
