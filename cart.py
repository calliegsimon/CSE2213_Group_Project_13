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

        view_query = f"SELECT ISBN, Title, Author, Quantity 
        FROM {self.table_name} INNER JOIN {inventoryDatabase} 
        ON {self.table_name}.ISBN = {inventoryDatabase}.ISBN
        WHERE UserID = {userID}"
        
        self.cursor.execute(view_query)

        # fetch all books in cart
        books = self.cursor.fetchall()

        print (f"{userID}'s cart:")
        
        # print the books in cart
        # expected to output ISBN, title, author, and quantity for each book in cart
        for book in books:
            print(book)

        # i think this is done, need to check that it runs as expected
    
    def addToCart(self, userID, ISBN):
        # use selected ISBN to add to user's cart

        # these two variables are created because of similarly named columns in the cart table
        bookID = ISBN
        customerID = userID

        # need to check that given book is in the right user's cart
        # updating quantity if book is already in the cart
        if bookID in Cart:
            add_query = f"UPDATE Cart SET Quantity = Quantity + 1 WHERE ISBN = {bookID}"
            self.cursor.execute(add_query, (f"%{bookID}%",))

        # if book is not already in cart
        else:
            self.cursor.execute("INSERT INTO Cart (UserID, ISBN, Quantity) VALUES (customerID, bookID, 1)")

        # save changes to table
        self.cursor.commit()


    def removeFromCart(self, userID, ISBN):
        # use selected ISBN to remove from user's cart
        if bookID in Cart:
            self.cursor.execute("UPDATE Cart SET Quantity = Quantity - 1 WHERE ISBN = bookID")
            self.cursor.execute("DELETE FROM Cart WHERE Quantity = '0'") # deletes the book from cart if quantity=0

        else: 
            print("Selected book is not in cart, so it's not possible to remove")

        # save changes
        self.cursor.commit()
        
    def checkOut(self, userID):
        # calls decreaseStock function from inventory class
        # removes all items in user's cart
        
        #decreaseStock(ISBN) for every book in cart
        
        # once all stock has been decreased
        checkOut_query = f"DELETE FROM {self.table_name} WHERE UserID = {userID}"
        self.cursor.execute(checkOut_query)

        # save changes
        self.cursor.commit()
