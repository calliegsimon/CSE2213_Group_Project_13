import sqlite3
con = sqlite3.connect("account.db")
cur = con.cursor()

loggedIn = False
username = ""
password = ""

def createAccount(username, password):
    matches = False
    global loggedIn, cur, con
    res = cur.execute("SELECT Username FROM Account")
    for name in res.fetchall():
        if name[0] == username:
            print("Username already exists. Please choose another.")
            matches = True
            break
    if matches is False:
        print("Username is unique! Please enter the following information: ")
        fullName = input("Your full name: ")
        fullAddress = input("Your full address (street, city, state zipcode): ")
        email = input("Your email address: ")
        payment = input("Your payment info (card number:)")
        isAdmin = int(input("Your admin status (0: not an admin 1: an admin): "))
        loggedIn = True
        cur.execute("""
                   INSERT INTO Account(Username, Password, Name, Address, Email, Payment, IsAdmin) VALUES
                       (?, ?, ?, ?, ?, ?, ?)""", (username, password, fullName, fullAddress, email, payment, isAdmin))
        con.commit()

def logIn(username, password):
    global loggedIn, cur, con
    info = cur.execute("SELECT Username, Password FROM Account")
    for name in info:
        if name[0] == username and name[1] == password:
            loggedIn = True
            break
    else:
        print("Error with username or password. Please try again.")

def logOut():
    global loggedIn
    if loggedIn is True:
        loggedIn = False
    else:
        print("How did you get this? You can't log out if you aren't logged in??")


# Account Creation
"""
while loggedIn is False:
    print("Welcome to ecommerce book store!")
    print("0. Create Account")
    print("1. Log In")
    choice = int(input("What would you like to do? "))
    while choice != 1 and choice != 0:
        print("Invalid input. Try again.")
        choice = int(input("What would you like to do? "))

    if choice == 0:
        print("")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        createAccount(username, password)

    elif choice == 1:
        print("")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        logIn(username, password)
"""












