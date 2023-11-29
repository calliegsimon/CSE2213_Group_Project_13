import sqlite3
import inventory

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

        view_query = f"SELECT {self.table_name}.ISBN, Title, Author, Quantity \
        FROM {self.table_name} INNER JOIN {inventoryDatabase} \
        ON {self.table_name}.ISBN = {inventoryDatabase}.ISBN WHERE UserID = '{userID}'"
        
        self.cursor.execute(view_query)

        # fetch all books in cart
        books = self.cursor.fetchall()

        print (f"{userID}'s cart:")
        
        # print the books in cart
        # expected to output ISBN, title, author, and quantity for each book in cart
        for i in books:
            print(i)

        # i think this is done, need to check that it runs as expected
    
    def addToCart(self, userID, ISBN):
        # use selected ISBN to add to user's cart

        # variables created because of similar names to columns in table
        customerID = userID
        bookID = ISBN

        checking_Cart = f"SELECT ISBN FROM {self.table_name} WHERE UserID = '{customerID}';"
        print(checking_Cart)
        self.cursor.execute(checking_Cart)

        customerCart = self.cursor.fetchall()

        # if cart is not empty
        if customerCart:
            # updating quantity if book is already in the cart
            if bookID in customerCart:
                print("in cart")
                add_query = f"UPDATE Cart SET Quantity = Quantity + 1 WHERE ISBN = '{bookID}';"
                self.cursor.execute(add_query)

            # if book is not already in cart
            else:
            print("not in cart")
            newbook_query = f"INSERT INTO {self.table_name} (UserID, ISBN, Quantity) VALUES ('{customerID}', '{bookID}', '1');"
            self.cursor.execute(newbook_query)

        else:
            adding_query = f"INSERT INTO {self.table_name} (UserID, ISBN, Quantity) VALUES ('{customerID}', '{bookID}', '1');"
            self.cursor.execute(adding_query)

        # save changes to table
        self.connection.commit()


    def removeFromCart(self, userID, ISBN):
        # use selected ISBN to remove from user's cart
        
        
        checkCart_query = f"SELECT ISBN FROM {self.table_name} where UserID = '{userID}';"
        self.cursor.execute(checkCart_query)

        userCart = self.cursor.fetchall()

        # checks that given book is in cart
        if ISBN in userCart:
            remove_query = f"UPDATE Cart SET Quantity = Quantity - 1 WHERE ISBN = '{ISBN}'"
            self.cursor.execute(remove_query)
            self.cursor.execute("DELETE FROM Cart WHERE Quantity = '0'") # deletes the book from cart if quantity=0

        else: 
            print("Selected book not in cart. Unable to remove.")

        # save changes
        self.connection.commit()
        
    def checkOut(self, userID):
        # calls decreaseStock function from inventory class
        # removes all items in user's cart
        
        cart_inven = inventory("Store_Database.db", "Inventory") # creates an inventory class object so we can call decreaseStock
        
        #decreaseStock(ISBN) for every book in cart
        decrease_query = f"SELECT ISBN, Quantity FROM {self.table_name} WHERE UserID = '{userID}'"
        self.cursor.execute(decrease_query)

        dec = self.cursor.fetchall()
        
        for row in dec:
            book = {self.table_name}.ISBN

            while {self.table_name}.Quantity > 0:
                cart_inven.decreaseStock(book)
                num_update = f"UPDATE Cart SET Quantity = Quantity - 1 WHERE ISBN = '{book}'"
                self.cursor.execute(num_update)
        
        # once all stock has been decreased
        checkOut_query = f"DELETE FROM {self.table_name} WHERE UserID = '{userID}'"
        self.cursor.execute(checkOut_query)

        # save changes
        self.connection.commit()

    def closeConnection(self):
        self.cursor.close()
        self.connection.close()
        
# outside class
myCart = cart("Store_Database.db", "Cart")
myCart.addToCart("anw734", 9781501142970)
myCart.viewCart("anw734", "Inventory")
myCart.closeConnection()


