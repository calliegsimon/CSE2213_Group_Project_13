"""
CONTENTS:
    account class has a create account method, which commits the input data into the table
    a login method, wherein a user logs into an already existing account
    a logout method, where a user is logged out
    a display method, which displays a user's information (aside from password)
    several edit methods, which replace the data both in the user object and in the table
"""
import sqlite3
con = sqlite3.connect("account.db")
cur = con.cursor()


class Account:
    def __init__(self):
        self.loggedIn = False
        self.username = ""
        self.password = ""
        self.fullName = ""
        self.fullAddress = ""
        self.email = ""
        self.payment = ""
        self.isAdmin = 0

    def createAccount(self, username, password):
        matches = False
        global cur, con
        res = cur.execute("SELECT Username FROM Account")
        for name in res.fetchall():
            if name[0] == username:
                print("Username already exists. Please choose another.")
                return False
        print("Username is unique! Please enter the following information: ")
        self.fullName = input("Your full name: ")
        self.fullAddress = input("Your full address (street, city, state zipcode): ")
        self.email = input("Your email address: ")
        self.payment = input("Your payment info (card number:)")
        self.isAdmin = int(input("Your admin status (0: not an admin 1: an admin): "))
        self.loggedIn = True
        cur.execute("""
            INSERT INTO Account(Username, Password, Name, Address, Email, Payment, IsAdmin) VALUES
            (?, ?, ?, ?, ?, ?, ?)""", (username, password, self.fullName, self.fullAddress, self.email, self.payment, self.isAdmin))
        con.commit()
        return True

    def logIn(self, username, password):
        global cur, con
        info = cur.execute("SELECT Username, Password FROM Account")
        for name in info:
            if name[0] == username and name[1] == password:
                data = cur.execute("SELECT Name, Address, Email, Payment, IsAdmin FROM Account WHERE Username = ?"), username
                self.loggedIn = True
                self.username = username
                self.password = password
                self.fullName = data[0]
                self.fullAddress = data[1]
                self.email = data[2]
                self.payment = data[3]
                self.isAdmin = data[4]
                return True
        print("Error with username or password. Please try again.")
        return False

    def logOut(self):
        if self.loggedIn is True:
            self.loggedIn = False
            return True
        else:
            print("How did you get this? You can't log out if you aren't logged in??")

    def displayAccount(self):
        print("")
        print("Username: " + self.username)
        print("Full name: " + self.fullName)
        print("Full address: " + self.fullAddress)
        print("Email: " + self.email)
        print("Payment info: " + self.payment)
        print("Admin status (0 not admin, 1 admin): " + str(self.isAdmin))

    def nameEdit(self, name):
        params = (name, self.username)
        self.fullName = name
        cur.execute("UPDATE Account SET Name=? WHERE Username=?", params)
        con.commit()

    def addressEdit(self, address):
        params = (address, self.username)
        self.fullAddress = address
        cur.execute("UPDATE Account SET Address=? WHERE Username=?", params)
        con.commit()

    def emailEdit(self, emailAd):
        params = (emailAd, self.email)
        self.email = emailAd
        cur.execute("UPDATE Account SET Email=? WHERE Username=?", params)
        con.commit()

    def paymentEdit(self, pay):
        params = (pay, self.payment)
        self.payment = pay
        cur.execute("UPDATE Account SET Payment=? WHERE Username=?", params)
        con.commit()

    def adminEdit(self, admin):
        params = (admin, self.isAdmin)
        self.isAdmin = admin
        cur.execute("UPDATE Account SET IsAdmin=? WHERE Username=?", params)
        con.commit()

    def deleteAccount(self):
        cur.execute("DELETE FROM Account WHERE Username=?", self.username)
        con.commit()
        self.loggedIn = False
        self.username = ""
        self.password = ""
        self.fullName = ""
        self.fullAddress = ""
        self.email = ""
        self.payment = ""
        self.isAdmin = 0

    def loginCheck(self):
        return self.loggedIn

    def getUsername(self):
        return self.username
con.close()
