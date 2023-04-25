This is a python program that scans products from a json file and emulates an online store. 
In this program, you can add products to your cart, delete them from your cart, and view your order summary.

How to install:
1. Install the file OnlineStore.exe along with Products.json.
2. Make sure to put OnlineStore.exe and Products.json in the same directory together, otherwise your products collection will be empty.
3. Run the executable file, and it should set up the rest assuming that you have MongoDB installed.

Dependencies:
- python
- mongodb
- Products.json

What could be improved:
If I were to continue working on this project, I would make a real user interface rather than making it a glorified command line.
This is a vague improvement, but I'm not entirely sure how I would make the user interface based on what I have now.
I would also add in more products rather than just 20 of them and perhaps make the json file parsed from the web rather than it being a local file.
This would get rid of an extra dependency in which the user needs to keep the Products.json file in the same place as the executable.
This could also eliminate the need for downloading a database unto your computer, which I assume is how the professionals do it.
I could also add more general features like being able to add more than one item at a time into the cart and getting a quantity of items rather than getting multiple one by one.
Overall, this project could be improved a lot if I had say 4 more weeks to work on it.
