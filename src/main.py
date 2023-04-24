"""Provides the main functionality and user interaction of the project."""
from user import User
from collection import collection
from json_parser import JsonParser
from products import ProductStock
from cart import ShoppingCart

EXIT_TERM = -1

def get_user_data() -> dict:
    """Prompts the user for their information and returns the answers in a dictionary."""
    user_data = {}
    data_list = ["first name", "last name", "date of birth", "email", "phone number"]
    for data in data_list:
        user_input = input(f"What's your {data}? ")
        user_data[data] = user_input
    return user_data

def main_menu(onlineStore : collection, products : ProductStock, user : User) -> None:
    """Serves as the main menu for the user by prompting them their options for the program."""
    user_input = 0
    cart = ShoppingCart(onlineStore.database["ShoppingCart"])
    while user_input != EXIT_TERM:
        try:
            user_input = int(input("What would you like to do?\n1. Shop for products.\n2. View your current cart.\n"
                                   f"(Type {EXIT_TERM} to quit) "))
            match user_input:
                case -1:
                    break
                case 1:
                    shopping(cart, products, user)
                case 2:
                    view_cart(cart, user)
                case _:
                    print("Not an option. Please try again.")
        except TypeError:
            print("Not an integer. Please try again.")

def shopping(cart : ShoppingCart, products : ProductStock, user : User) -> None:
    """Prompts the user for a category to select a product from and then gets their selection."""
    category = ""
    while True:
        category = input(f"What category would you like to search? (Type {EXIT_TERM} to quit) ")
        if category == str(EXIT_TERM):
            break
        product_list = products.get_products_in(category)
        print_products(product_list)
        cart.insert_into_cart(user.pnumber, get_selection(product_list))

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

def view_cart(cart : ShoppingCart, user : User) -> None:
    user_cart = cart.get_user_cart(user.pnumber)
    print(f"{user.fname} {user.lname}'s cart: ")
    for product in user_cart:
        print(f"id: {product['id']}, title: {product['title']}, category: {product['category']}, price: {product['price']}.")

def main() -> None:
    """The main function that initializes everything at the beginning"""
    online_store = collection()
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
