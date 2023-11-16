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
            elif user_choice == "3":
                # add in logic for viewing cart information
            elif user_choice == "4":
                print("Bye!")
                break
            else:
                print("Invalid choice. Try again.")
    
