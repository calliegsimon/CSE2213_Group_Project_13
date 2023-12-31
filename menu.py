import inventory
import cart
import account

#creating class objects and variables
acct = account.Account()
myCart = cart.cart('Store_Database.db', 'Cart')
storeInven = inventory.Inventory('Store_Database.db', 'Inventory')
username = ""
password = ""

def afterLogin():
        # after login menu
        while acct.loginCheck() is True:
                print("Main Menu")
                print("1. View Account Information")
                print("2. Inventory Information")
                print("3. Cart Information")
                print("4. Logout")

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                        while True:
                                acct.displayAccount()
                                print("1. Go back")
                                print("2. Edit name")
                                print("3. Edit address")
                                print("4. Edit email address")
                                print("5. Edit payment info")
                                print("6. Delete account")
                                acct_choice = int(input("Enter your choice: "))

                                if acct_choice == 1:
                                        break
                                elif acct_choice == 2:
                                        name = input("Enter the new name: ")
                                        acct.nameEdit(name)
                                elif acct_choice == 3:
                                        add = input("Enter the new address: ")
                                        acct.addressEdit(add)
                                elif acct_choice == 4:
                                        email = input("Enter the new email address: ")
                                        acct.emailEdit(email)
                                elif acct_choice == 5:
                                        pay = input("Enter the new payment information: ")
                                        acct.paymentEdit(pay)
                                elif acct_choice == 6:
                                        acct.deleteAccount()
                                        break
                                else:
                                        print("Invalid option. Try again.")
                        
                elif user_choice == 2:
                    # inventory menu
                    print("Invetory Information Menu")
                    print("1. Go Back")
                    print("2. View Inventory")
                    print("3. Search Inventory")


                    inv_choice = int(input("Please enter your choice:  "))

                    if inv_choice == 1:
                        #go back
                        break
                        # adding the break statement should return it back to the main menu. 
                    elif inv_choice == 2:
                        inventory.viewInventory()
                    elif inv_choice == 3:
                        print("Please enter the title of the book you are looking for: ")
                        search_title = str(input("Please enter the title of the book you are looking for: "))
                        inventory.searchInventory(search_title)
                    else:
                        print("Invalid choice.")

                elif user_choice == 3:
                    # cart menu
                    print("Cart Information Menu")
                    print("1. Go Back")
                    print("2. View Cart")
                    print("3. Add Items to Cart")
                    print("4. Remove an Item From Cart")
                    print("5. Check Out")

                    userID = acct.getUsername()
                    cart_choice = int(input("Enter your choice: "))
                    
                    if cart_choice == 1:
                        # go back
                        break
                
                    elif cart_choice == 2:
                        # view cart
                        myCart.viewCart(userID, "Inventory") 

                    elif cart_choice == 3:
                        # add to cart
                        storeInven.viewInventory()
                        book_add = int(input("Enter the ISBN of the book you want to add to your cart: "))
                        myCart.addToCart(userID, book_add)

                    elif cart_choice == 4:
                        # remove from cart
                        myCart.viewCart(userID, 'Store_Database.db') # same note as when cart_choice == "2"
                        book_remove = int(input("Enter the ISBN of the book you want to remove from your cart: "))
                        myCart.removeFromCart(userID, book_remove)
                        
                    elif cart_choice == 5:
                        # check out
                        myCart.checkOut(userID)
                        
                    else:
                        print("Invalid choice.")
                
                elif user_choice == 4:
                        if acct.logOut() == True:
                                print("You are logged out. Bye!")
                                break
                else:
                    print("Invalid choice. Try again.")
    

# before login menu
while True:
        print("Welcome to our online store!")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")


        user_choice = int(input("Please enter what you would like to do: "))

        if user_choice == 1:
                # login
                username = input("Please enter your username: ")
                password = input("Please enter your password: ")
                acct.logIn(username, password)
                if acct.logIn(username, password) == True:
                        print("You are logged in!")
                        afterLogin() # should take user to after login menu
                else:
                        print("Login unsuccessful.")
                        
        elif user_choice == 2:
                # create account 
                username = input("What would you like your username to be? ")
                password = input("What would you like your password to be? ")
                acct.createAccount(username, password)
                if acct.loginCheck is True:     
                        print("Account has been created, and you have been logged in.")
                        afterLogin() # takes user to after login menu
                        
        elif user_choice == 3:
                #i figure this should be fine because there's no way to get to the acct creation/login screen while logged in. 
                print("Bye!")
                break
                
        else:
                print("Invalid choice. Try again.")

myCart.closeConnection()
storeInven.close_connection()

                break
                
        else:
                print("Invalid choice. Try again.")
