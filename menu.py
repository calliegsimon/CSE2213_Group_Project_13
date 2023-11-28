import sqlite3
import inventory
import cart

class Menu:
    def __init__(self):
        self.loggedin = False # placeholder for the time being.
        #be sure to implement the user sign in/ authentication

    def before_login_menu(self):
        while True:
            print("Welcome to our online store:")
            print("1. Login")
            print("2. Create Account")
            print("3. Exit")

            user_choice = int(input("Please enter what you would like to do: "))

            if user_choice == "1":
                if not self.loggedin:
                    self.login()
                else:
                    print("You're already logged in.")
            elif user_choice == "2":
                # create account function name. self.create_account or something like that
            elif user_choice == "3":
                print("Bye!")
                break
            else:
                print("Invalid choice. Try again.")

    def after_login_menu(self):
        while True:
            print("Here i")
            print("1. View Account Information")
            print("2. Inventory Information")
            print("3. Cart Information")
            print("4. Logout")

            user_choice = int(input("Enter your choice: "))

            if user_choice == "1":
                #add in logic for viewing account info
            elif user_choice == "2":
                # add in logic for looking at inventory infortmation
                print("Invetory Information Menu")
                print("-" * 50)
                print("1. Go Back")
                print("2. View Inventory")
                print("3. Search Inventory")


                inv_choice = int(input("Please enter your choice:  "))

                if inv_choice == "1":
                    #go back
                    break
                    # adding the break statement should return it back to the main menu. 
                elif inv_choice == "2":
                    inventory.viewInventory()
                elif inv_choice == "3":
                    print("Please enter the title of the book you are looking for: ")
                    search_title = str(input("Please enter the title of the book you are looking for: "))
                    inventory.searchInventory(search_title)
                else:
                    print("Invalid choice.")

            elif user_choice == "3":
                # cart information
                print("Cart Information Menu")
                print("1. Go Back")
                print("2. View Cart")
                print("3. Add Items to Cart")
                print("4. Remove an Item From Cart")
                print("5. Check Out")

                cart_choice = int(input("Enter your choice: "))

                myCart = cart('Store_Database.db', 'Cart')  # creates a cart class object
                                                                # do we need to move this to a main file?
                    
                if cart_choice == "1":
                    # go back
                elif cart_choice == "2":
                    # view cart
                    myCart.viewCart(userID, 'Store_Database.db') # does "Store_Database.db" need to be changed to "Cart"

                elif cart_choice == "3":
                    # add to cart
                    myInventory.viewInventory()
                    book_add = int(input("Enter the ISBN of the book you want to add to your cart: "))
                    myCart.addToCart(userID, book_add)

                elif cart_choice == "4":
                    # remove from cart
                    myCart.viewCart(userID, 'Store_Database.db') # same note as when cart_choice == "2"
                    book_remove = int(input("Enter the ISBN of the book you want to remove from your cart: "))
                    myCart.removeFromCart(userID, book_remove)
                        
                elif cart_choice == "5":
                    # check out
                    myCart.checkOut(userID)
                        
                else:
                    print("Invalid choice.")
                
            elif user_choice == "4":
                print("Bye!")
                break
            else:
                print("Invalid choice. Try again.")
    
