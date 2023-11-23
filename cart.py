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

        # select data from cart table
        self.cursor.execute("SELECT ISBN, Quantity FROM Cart WHERE UserID = userID")

        # select data from cart table
        

        # fetch all books in cart
        books = self.cursor.fetchall()

        print (f"{userID}'s cart:")
        
        # print the books in cart
        for book in books:
            print (book) # only prints ISBN and Quantity
                         # need to fix to print Title and Author too (get from InventoryDB)
            
        print (f"ISBN: {ISBN}, Title: {}, Author: {Author}, Quantity: {Quantity}")

    def addToCart(self, userID, ISBN):
        # use selected ISBN to add to user's cart

        # these two variables are created because of similarly named columns in the cart table
        bookID = ISBN
        customerID = userID

        # updating quantity if book is already in the cart
        if bookID in Cart:
            self.cursor.execute("UPDATE Cart SET Quantity = Quantity + 1 WHERE ISBN = bookID")

            # if book is not already in cart
            else:
                self.cursor.execute("INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (customerID, bookID, 1)")

        # save changes to table
        self.cursor.commit()


    def removeFromCart(self, userID, ISBN):
        # use selected ISBN to remove from user's cart
        
    def checkOut(self, userID):
        # calls decreaseStock function from inventory class
        # removes all items in user's cart
