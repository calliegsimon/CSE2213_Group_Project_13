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
    
    def addToCart(self, userID, ISBN):
        # use selected ISBN to add to user's cart

        # variables created because of similar names to columns in table
        customerID = userID
        bookID = ISBN

        checking_Cart = f"SELECT {self.table_name}.ISBN FROM {self.table_name} WHERE UserID = '{customerID}';"
        self.cursor.execute(checking_Cart)

        customerCart = self.cursor.fetchall()
        
        # if cart is not empty
        if customerCart:

            # searches for given book in cart
            update_query = f"SELECT * FROM {self.table_name} WHERE ISBN LIKE '{bookID}';"
            self.cursor.execute(update_query)
            alreadyThere = self.cursor.fetchall()

            # if book is already in the cart
            if alreadyThere:
                add_query = f"UPDATE {self.table_name} SET Quantity = Quantity+1 WHERE ISBN = '{bookID}';"
                self.cursor.execute(add_query)

            # if book is not already in cart
            else:
                newbook_query = f"INSERT INTO {self.table_name} (UserID, ISBN, Quantity) VALUES ('{customerID}', '{bookID}', '1');"
                self.cursor.execute(newbook_query)

        else:
            adding_query = f"INSERT INTO {self.table_name} (UserID, ISBN, Quantity) VALUES ('{customerID}', '{bookID}', '1');"
            self.cursor.execute(adding_query)

        # save changes to table
        self.connection.commit()


    def removeFromCart(self, userID, ISBN):
        # use selected ISBN to remove from user's cart
        # self.cursor.execute('''DELETE FROM Cart''')
        bookID = str(ISBN)

        checkCart_query = f"SELECT {self.table_name}.ISBN FROM {self.table_name} WHERE UserID = '{userID}';"
        self.cursor.execute(checkCart_query)

        userCart = self.cursor.fetchall()

        # checks that cart isn't already empty
        if userCart:

            # searches for given book in cart
            update_query = f"SELECT * FROM {self.table_name} WHERE ISBN LIKE '{bookID}';"
            self.cursor.execute(update_query)
            foundBook = self.cursor.fetchall()

            # checks that given book is in cart
            if foundBook:
                remove_query = f"UPDATE {self.table_name} SET Quantity = Quantity - 1 WHERE ISBN = '{bookID}';"
                self.cursor.execute(remove_query)
                self.cursor.execute("DELETE FROM Cart WHERE Quantity=0;") # deletes the book from cart if quantity=0

            else: 
                print("Selected book not in cart. Unable to remove.")

        else:
            print("Cart is empty. Nothing to remove.")

        # save changes
        self.connection.commit()
        
    def checkOut(self, userID):
        # calls decreaseStock function from inventory class
        # removes all items in user's cart
        
        # creates an inventory class object so we can call decreaseStock
        cart_inven = inventory.Inventory("Store_Database.db", "Inventory") 
        
        #decreaseStock(ISBN) for every book in cart
        decrease_query = f"SELECT ISBN, Quantity FROM {self.table_name} WHERE UserID = '{userID}'"
        self.cursor.execute(decrease_query)

        dec = self.cursor.fetchall()
        
        for book in dec:
            i = book[1]
            while i > 0:              
                bookISBN = str(book[0])
                print(bookISBN)
                cart_inven.decreaseStock(str(bookISBN))
                i = i - 1
        
        # once all stock has been decreased
        checkOut_query = f"DELETE FROM {self.table_name} WHERE UserID = '{userID}'"
        self.cursor.execute(checkOut_query)

        # save changes
        self.connection.commit()

    def closeConnection(self):
        self.cursor.close()
        self.connection.close()
