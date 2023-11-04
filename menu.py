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

            user_choice = input("Please enter what you would like to do: ")

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
