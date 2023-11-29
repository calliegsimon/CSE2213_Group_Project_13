import sqlite3



class Inventory:
    # class constructor
    def __init__(self, db_name, table_name):
        # storing the database name and table names as attributes
        self.db_name = db_name # database name for SQLite db
        self.table_name = table_name # name of the table in database
        self.connection = sqlite3.connect(self.db_name) # establishes a connection to the db and returns a connection object
        self.cursor = self.connection.cursor() # this creates a curor to interaction with the db
        # note: a cursor allows you to execute your sql queries
        
    def decreaseStock(self, ISBN): # the decrease stock method, decreases the stock quantity of a product in the inventory by one
        #Called with a single ISBN parameter and decreases the
        #stock number in the appropriate database for the appropriate ISBN


        # make a sql update query to decrease the quantity of a product in the table by one
        # `self.table_name` is the name of the table where product information is stored
        # the 'stock' column should be decreased by 1 for the product with a matching ISBN
        update_query = f"UPDATE {self.table_name} SET Stock = Stock - 1 WHERE ISBN = ?;"
        self.cursor.execute(update_query, (ISBN,)) #executes the query using the cursor and uses isbn as a parameter to be inserted into the query
        # the `execute` method of the cursor runs the sql query with the provided parameter(s)

        # commit the updates to the db
        self.connection.commit()
        # the `commit` method is called to save the changes made to the database

    def viewInventory(self): 
        # method to display all of the items in the inventory
        #Displays all items in the inventory in some formatted way
        
        # make a sql select query in order to get all the data from the table
        select_q = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(select_q)

        #get all results from the table
        products = self.cursor.fetchall()

        #create an if loop for if there are products found (There definitely should be lol)
        if products:
            #set up the format for printing out the inventory
            
            # for loop to iterate through the products and display all of the info 
            for product in products:
               # if there are products iterate through each product and print their info
                print(f"ISBN: {product[0]}, Title: {product[1]}, Author: {product[2]}, Genre: {product[3]}, Pages: {product[4]}, ReleaseDate: {product[5]}, Stock: {product[6]}")
        else:
            print("Your inventory is empty")

    def searchInventory(self, title):
        # method in order to search for specfic products based on titles
        #Asks for a *title*, checks the database to see if a result is returned on
        #that name. If so, display all results. If not, the user is informed their search failed
        search_query = f"SELECT * FROM {self.table_name} WHERE Title LIKE ?;"# make a sql select query in order to get all the data from the table
        self.cursor.execute(search_query, (f"%{title}%",))# execute the sql query using the cursor and parameters
        products = self.cursor.fetchall() # fetch all the results returned by the query
        if products:
            for product in products:
               # if there are products iterate through each product and print their info
                print(f"ISBN: {product[0]}, Title: {product[1]}, Author: {product[2]}, Genre: {product[3]}, Pages: {product[4]}, ReleaseDate: {product[5]}, Stock: {product[6]}")
        else:
            # if there are no products
            print(f"No products found with the title: {title}")

    def close_connection(self):
        # method to close the connection to the sqlite db
        self.cursor.close()
        #close the db connection
        self.connection.close()
        # the 'close' method is called on the connection object to terminate the connection


    # getters and setters
    def get_db_name(self):
        return self.db_name
    
    def set_db_name(self, new_db_name):
        self.db_name = new_db_name

    def get_table_name(self):
        return self.table_name
    
    def set_table_name(self, new_table_name):
        self.table_name = new_table_name

