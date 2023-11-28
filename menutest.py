loggedIn = False
isAdmin = True
while True:
    print("Welcome to ecommerce store!")
    print("0. Create account")
    print("1. Log In")
    print("2. Exit")
    choice = int(input("Enter the number of what you'd like to do: "))
    if choice != 0 and choice != 1 and choice != 2:
        print("That isn't an option. Try again.")
    elif choice is 0:
        print("")
        print("account creation placeholder")
        loggedIn = True
    elif choice is 1:
        print("")
        print("log in placeholder")
        loggedIn = True
    elif choice is 2:
        break
    while loggedIn is True:
        print("")
        print("0. Log out")
        print("1. Cart Information")
        print("2. Inventory")
        print("3. Account Information")
        print("4. Order History")
        choice = int(input("Enter the number of what you'd like to do: "))
        if choice < 0 or choice > 4:
            print("That isn't an option. Try again.")
        if choice is 0:
            print("logout")
            loggedIn = False
            break
        elif choice is 1:
            print("")
            print("0. Go back")
            print("1. View cart")
            print("2. Remove item from cart")
            print("3. Add item to cart")
            print("4. Edit item quantity in cart")
            print("5. Check out with current cart")
            choice = int(input("Enter the number of what you'd like to do: "))
            if choice < 0 or choice > 5:
                print("That isn't an option. Try again.")
            elif choice is 1:
                print("viewing cart")
            elif choice is 2:
                print("removing item from cart")
            elif choice is 3:
                print("adding item to cart")
            elif choice is 4:
                print("editing item quantity")
            elif choice is 5:
                print("checking out")
        elif choice is 2:
            print("")
            print("0. Go back")
            print("1. View inventory")
            print("2. Search inventory")
            if isAdmin is True:
                print("3. Add item to inventory")
                print("4. Remove item from inventory")
            choice = int(input("Enter the number of what you'd like to do: "))
            if choice < 0 or choice > 4:
                print("That isn't an option. Try again.")
            elif choice is 1:
                print("viewing inventory")
            elif choice is 2:
                print("searching inventory")
            elif choice is 3:
                print("adding item to inventory")
            elif choice is 4:
                print("removing item from inventory")
        elif choice is 3:
            print("")
            print("0. Go back")
            print("1. Edit address")
            print("2. Edit payment method")
            print("3. Delete account")
            choice = int(input("Enter the number of what you'd like to do: "))
            if choice < 0 or choice > 3:
                print("That isn't an option. Try again.")
            elif choice is 1:
                print("editing address")
            elif choice is 2:
                print("editing payment info")
            elif choice is 3:
                print("deleting account")
                loggedIn = False
        elif choice is 4:
            print("")
            print("0. Go back")
            print("1. View order history")
            print("2. Cancel order")
            choice = int(input("Enter the number of what you'd like to do: "))
            if choice < 0 or choice > 2:
                print("That isn't an option. Try again.")
            elif choice is 1:
                print("order history")
            elif choice is 2:
                print("Cancelling order")

