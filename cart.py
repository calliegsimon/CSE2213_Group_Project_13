import sqlite3
import sys

try:
    connection = sqlite3.connect(Store_Database.db)
    print("successful connection")

except:
    print("failed connection")
    sys.exit()


# makes cart class
class cart:

    #constructor
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def viewCart(self, userID, inventoryDatabase):
        # displays all books in logged in user's cart

    def addToCart(self, userID, ISBN):
        # use selected ISBN to add to user's cart

        # these two variables are created because of similarly named columns in the cart table
        bookID = ISBN
        customerID = userID

        # updating quantity if book is already in the cart
        if bookID in Cart:
            self.cursor.execute(UPDATE Cart SET Quantity = Quantity + 1 WHERE ISBN = bookID)

            # if book is not already in cart
            else:
                self.cursor.execute(INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (customerID, bookID, 1))


    def removeFromCart(self, userID, ISBN):
        # use selected ISBN to remove from user's cart
        
    def checkOut(self, userID):
        # calls decreaseStock function from inventory class
        # removes all items in user's cart
