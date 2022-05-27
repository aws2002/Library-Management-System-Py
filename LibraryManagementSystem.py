import datetime
import os

# import fileinput

os.getcwd()


class LibraryManagementSystem:
    def __init__(self, listOfBooks, listOfUser, libraryName):
        self.listOfBooks = listOfBooks
        self.listOfUser = listOfUser
        self.libraryName = libraryName
        self.booksDict = {}
        self.userDict = {}
        idBooks = 101
        idUser = 101
        with open(self.listOfBooks) as b:
            content = b.readlines()
        for line in content:
            title, status, newAuthor, price, rackNo, quantity = line.strip().split(",")
            self.booksDict.update(
                {
                    str(idBooks): {
                        "booksTitle": title,
                        "lenderName": "",
                        "lendDate": "",
                        "status": status,
                        "author": newAuthor,
                        "price": price + "$",
                        "quantity": quantity,
                        "rackNo": rackNo,
                        # "lenderID": "",
                        # "lenderAddress": "",
                    }
                }
            )
            idBooks += 1

        with open(self.listOfUser) as a:
            c = a.readlines()
        for lines in c:
            ids, name, address, password = lines.strip().split(",")
            self.userDict.update(
                {
                    str(idUser): {
                        "id": ids,
                        "name": name,
                        "address": address,
                        "password": password,
                    }
                }
            )
        idUser += 1

    def addUser(self):
        newUser = input("Enter a name : ")
        idUser = input("Enter a id : ")
        address = input("Enter a address : ")
        password = input("Enter a password : ")

        if newUser == "" and idUser == "" and address == "" and password == "":
            return self.addBooks()
        elif len(newUser) > 20 and len(address) > 20:
            print(
                "❌❌❌ Books title or Author name length is too long !? Title length limit is 20 characters ❌❌❌"
            )
            return self.addUser()
        else:
            with open(self.listOfUser, "a") as b:
                b.writelines(f"{idUser},{newUser},{address},{password}\n")
            self.userDict.update(
                {
                    str(int(max(self.userDict)) + 1): {
                        "id": idUser,
                        "name": newUser,
                        "address": address,
                        "password": password,
                    }
                }
            )
            print(f"✅✅✅ The books '{newUser}' has been added successfully ✅✅✅")

    def displayBooks(self):
        print(
            "---------------------------------------------- 📖 List of Books 📖 ---------------------------------------------------------------"
        )
        print(
            "{0:^1}{1:>16s}{2:>17s}{3:>19s}{4:>19s}{5:>19s}{6:>19s}".format(
                "Books key", "Title", "Status", "Author", "Price", "RackNo", "Quantity"
            )
        )
        print(
            "---------------------------------------------------------------------------------------------------------------------------------"
        )
        for key, value in self.booksDict.items():
            print(
                "{0:^1}{1:>21s}{2:>20s}{3:>13s}{4:>19s}{5:>18s}{6:>16s}".format(
                    key,
                    value.get("booksTitle"),
                    value.get("status"),
                    value.get("author"),
                    value.get("price"),
                    value.get("rackNo"),
                    value.get("quantity"),
                )
            )

    def displayUser(self):
        print(
            "---------------------------------------------- 👤 List of Users 👤 ---------------------------------------------------------------"
        )
        print(
            "{0:^1}{1:>16s}{2:>17s}{3:>19s}".format(
                "User key", "Name", "Pssword", "Address", "ID"
            )
        )
        print(
            "---------------------------------------------------------------------------------------------------------------------------------"
        )
        for keys, value in self.userDict.items():
            print(
                "{0:^1}{1:>21s}{2:>20s}{3:>13s}".format(
                    keys,
                    value.get("name"),
                    value.get("password"),
                    value.get("address"),
                    value.get("id"),
                )
            )

    def showIssuedBooks(self):
        print(
            "------------------------ 📖 List of show issued books 📖 ----------------------------------------------------"
        )
        print(
            "{0:^1}{1:>16s}{2:>19s}{3:>19s}{4:>19s}{5:>19s}".format(
                "Books key", "Title", "Author", "Price", "RackNo", "Quantity"
            )
        )
        print(
            "-------------------------------------------------------------------------------------------------------------"
        )

        for key, value in self.booksDict.items():
            if value.get("status") == "Available":
                print(
                    "{0:^1}{1:>21s}{2:>16s}{3:>20s}{4:>19s}{5:>18s}".format(
                        key,
                        value.get("booksTitle"),
                        value.get("author"),
                        value.get("price"),
                        value.get("rackNo"),
                        value.get("quantity"),
                    )
                )

    def issueBooks(self):
        def check(name, password, bookID):
            with open("user.txt") as f:
                if name and password in f.read():
                    # userID = input("Enter Your ID : ")
                    print("✅✅✅ User data verification process ✅✅✅")
                    # userAddress = input("Enter Your Address : ")
                    self.booksDict[bookID]["lenderName"] = yourName
                    self.booksDict[bookID]["lendDate"] = currentDate
                    self.booksDict[bookID]["status"] = "Already Issued"
                    # self.booksDict[booksID]["lenderID"] = userID
                    # self.booksDict[booksID]["lenderAddress"] = userAddress
                    print("✅✅✅ Book Issued Successfully ✅✅✅\n")
                else:
                    print("❌❌❌ User Not Found ❌❌❌")

        booksID = input("Enter Books ID : ")
        currentDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if booksID in self.booksDict.keys():
            if not self.booksDict[booksID]["status"] == "Available":
                print(
                    f"🤔🤔🤔 This book is already issued to {self.booksDict[booksID]['lenderName']} on {self.booksDict[booksID]['lendDate']}"
                )
                return self.issueBooks()
            elif self.booksDict[booksID]["status"] == "Available":
                yourName = input("Enter Your Name : ")
                userPassword = input("Enter Your Password : ")
                check(name=yourName, password=userPassword, bookID=booksID)
        else:
            print("❌❌❌ Book ID Not Found ❌❌❌")
            return self.issueBooks()

    def deleteUser(self):
        userID = int(input("Enter User ID to delete it : "))
        try:
            file = open("user.txt", "r")
            lines = file.readlines()
            del lines[userID - 101]
            newFile = open("user.txt", "w+")
            for line in lines:
                newFile.write(line)
            print("✅✅✅ User deleted Successfully ✅✅✅\n")
        except Exception as e:
            print("❌❌❌ User ID Not Found ❌❌❌")
            return self.deleteUser()

    def deleteBooks(self):
        booksID = int(input("Enter Books ID to delete it : "))
        try:
            file = open("listOfBooks.txt", "r")
            lines = file.readlines()
            del lines[booksID - 101]
            newFile = open("listOfBooks.txt", "w+")
            for line in lines:
                newFile.write(line)
            print("✅✅✅ Book deleted Successfully ✅✅✅\n")
        except Exception as e:
            print("❌❌❌ Book ID Not Found ❌❌❌")
            return self.deleteBooks()

    def updateBook(self):
        booksID = input("Enter Books key : ")
        if booksID in self.booksDict.keys():
            print("What want you to update book")
            pressKeyListForUpdat = {
                "1": "Edit name",
                "2": "Edit author",
                "3": "Edit price",
                "4": "Edit quantity",
                "5": "Edit rackNo",
                "6": "Exit",
            }
            for key, value in pressKeyListForUpdat.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "1":
                print("\nCurrent Selection : EDIT NAME\n")
                oldData = input("Enter a old name : ")
                newData = input("Enter a new name : ")
                with open(r"listOfBooks.txt", "r") as file:
                    data = file.readlines()[int(booksID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"listOfBooks.txt", "a") as file:
                    file.write(data)
                file = open("listOfBooks.txt", "r")
                lines = file.readlines()
                del lines[int(booksID) - 101]
                newFile = open("listOfBooks.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.booksDict.update(
                    {
                        str(int(booksID)): {
                            "booksTitle": newData,
                            "lenderName": self.booksDict[booksID]["lenderName"],
                            "lendDate": self.booksDict[booksID]["lendDate"],
                            "status": self.booksDict[booksID]["status"],
                            "author": self.booksDict[booksID]["author"],
                            "price": self.booksDict[booksID]["price"],
                            "quantity": self.booksDict[booksID]["quantity"],
                            "rackNo": self.booksDict[booksID]["rackNo"],
                            # "lenderID": self.booksDict[booksID]["lenderID"],
                            # "lenderAddress": self.booksDict[booksID]["lenderAddress"],
                        }
                    }
                )

            elif key_press == "2":
                print("\nCurrent Selection : EDIT AUTHOR\n")
                oldData = input("Enter a old author : ")
                newData = input("Enter a new author : ")
                with open(r"listOfBooks.txt", "r") as file:
                    data = file.readlines()[int(booksID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"listOfBooks.txt", "a") as file:
                    file.write(data)
                file = open("listOfBooks.txt", "r")
                lines = file.readlines()
                del lines[int(booksID) - 101]
                newFile = open("listOfBooks.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.booksDict.update(
                    {
                        str(int(booksID)): {
                            "booksTitle": self.booksDict[booksID]["booksTitle"],
                            "lenderName": self.booksDict[booksID]["lenderName"],
                            "lendDate": self.booksDict[booksID]["lendDate"],
                            "status": self.booksDict[booksID]["status"],
                            "author": newData,
                            "price": self.booksDict[booksID]["price"],
                            "quantity": self.booksDict[booksID]["quantity"],
                            "rackNo": self.booksDict[booksID]["rackNo"],
                            # "lenderID": self.booksDict[booksID]["lenderID"],
                            # "lenderAddress": self.booksDict[booksID]["lenderAddress"],
                        }
                    }
                )
            elif key_press == "3":
                print("\nCurrent Selection : EDIT PRICE\n")
                oldData = input("Enter a old price : ")
                newData = input("Enter a new price : ")
                with open(r"listOfBooks.txt", "r") as file:
                    data = file.readlines()[int(booksID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"listOfBooks.txt", "a") as file:
                    file.write(data)
                file = open("listOfBooks.txt", "r")
                lines = file.readlines()
                del lines[int(booksID) - 101]
                newFile = open("listOfBooks.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.booksDict.update(
                    {
                        str(int(booksID)): {
                            "booksTitle": self.booksDict[booksID]["booksTitle"],
                            "lenderName": self.booksDict[booksID]["lenderName"],
                            "lendDate": self.booksDict[booksID]["lendDate"],
                            "status": self.booksDict[booksID]["status"],
                            "author": self.booksDict[booksID]["author"],
                            "price": newData,
                            "quantity": self.booksDict[booksID]["quantity"],
                            "rackNo": self.booksDict[booksID]["rackNo"],
                            # "lenderID": self.booksDict[booksID]["lenderID"],
                            # "lenderAddress": self.booksDict[booksID]["lenderAddress"],
                        }
                    }
                )
            elif key_press == "4":
                print("\nCurrent Selection : EDIT QUANTITY\n")
                oldData = input("Enter a old quantity : ")
                newData = input("Enter a new quantity : ")
                with open(r"listOfBooks.txt", "r") as file:
                    data = file.readlines()[int(booksID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"listOfBooks.txt", "a") as file:
                    file.write(data)
                file = open("listOfBooks.txt", "r")
                lines = file.readlines()
                del lines[int(booksID) - 101]
                newFile = open("listOfBooks.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.booksDict.update(
                    {
                        str(int(booksID)): {
                            "booksTitle": self.booksDict[booksID]["booksTitle"],
                            "lenderName": self.booksDict[booksID]["lenderName"],
                            "lendDate": self.booksDict[booksID]["lendDate"],
                            "status": self.booksDict[booksID]["status"],
                            "author": self.booksDict[booksID]["author"],
                            "price": self.booksDict[booksID]["price"],
                            "quantity": newData,
                            "rackNo": self.booksDict[booksID]["rackNo"],
                            # "lenderID": self.booksDict[booksID]["lenderID"],
                            # "lenderAddress": self.booksDict[booksID]["lenderAddress"],
                        }
                    }
                )
            elif key_press == "5":
                print("\nCurrent Selection : EDIT RackNo\n")
                oldData = input("Enter a old RackNo : ")
                newData = input("Enter a new RackNo : ")
                with open(r"listOfBooks.txt", "r") as file:
                    data = file.readlines()[int(booksID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"listOfBooks.txt", "a") as file:
                    file.write(data)
                file = open("listOfBooks.txt", "r")
                lines = file.readlines()
                del lines[int(booksID) - 101]
                newFile = open("listOfBooks.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.booksDict.update(
                    {
                        str(int(booksID)): {
                            "booksTitle": self.booksDict[booksID]["booksTitle"],
                            "lenderName": self.booksDict[booksID]["lenderName"],
                            "lendDate": self.booksDict[booksID]["lendDate"],
                            "status": self.booksDict[booksID]["status"],
                            "author": self.booksDict[booksID]["author"],
                            "price": self.booksDict[booksID]["price"],
                            "quantity": self.booksDict[booksID]["quantity"],
                            "rackNo": newData,
                            # "lenderID": self.booksDict[booksID]["lenderID"],
                            # "lenderAddress": self.booksDict[booksID]["lenderAddress"],
                        }
                    }
                )
            elif key_press == "6":
                exit()

            print("✅✅✅ Update Book Successfully ✅✅✅\n")
        else:
            print("❌❌❌ Book ID Not Found ❌❌❌")
            return self.updateBook()

    def addBooks(self):
        newBooks = input("Enter Books Title : ")
        newAuthor = input("Enter a author : ")
        price = input("Enter a price : ")
        quantity = input("Enter a quantity : ")
        rackNo = input("Enter a Rack-No : ")
        if (
            newBooks == ""
            and rackNo == ""
            and quantity == ""
            and price == ""
            and newAuthor == ""
        ):
            return self.addBooks()
        elif len(newBooks) > 20 and len(newAuthor) > 20:
            print(
                "❌❌❌ Books title or Author name length is too long !? Title length limit is 20 characters ❌❌❌"
            )
            return self.addBooks()
        else:
            with open(self.listOfBooks, "a") as b:
                b.writelines(
                    f"{newBooks},Available,{newAuthor},{price},{rackNo},{quantity}\n"
                )
            self.booksDict.update(
                {
                    str(int(max(self.booksDict)) + 1): {
                        "booksTitle": newBooks,
                        "lenderName": "",
                        "lendDate": "",
                        "status": "Available",
                        "author": newAuthor,
                        "price": price,
                        "quantity": quantity,
                        "rackNo": rackNo,
                        # "lenderID": "",
                        # "lenderAddress": "",
                    }
                }
            )
            print(f"✅✅✅ The books '{newBooks}' has been added successfully ✅✅✅")

    def returnBooks(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.booksDict.keys():
            if self.booksDict[books_id]["status"] == "Available":
                print(
                    "❌❌❌ This book is already available in library. Please check book id ❌❌❌"
                )
                return self.return_books()
            elif not self.booksDict[books_id]["status"] == "Available":
                self.booksDict[books_id]["lenderName"] = ""
                self.booksDict[books_id]["lendDate"] = ""
                # self.booksDict[books_id]["lenderID"] = ""
                # self.booksDict[books_id]["lenderAddress"] = ""
                self.booksDict[books_id]["status"] = "Available"
                print("✅✅✅ Successfully Updated ✅✅✅\n")
        else:
            print("❌❌❌ Book ID Not Found ❌❌❌")

    def updateUser(self):
        userID = input("Enter User key : ")
        if userID in self.userDict.keys():
            print("What want you to update user")
            pressKeyListForUpdat = {
                "1": "Edit name",
                "2": "Edit id",
                "3": "Edit password",
                "4": "Edit address",
                "5": "Exit",
            }
            for key, value in pressKeyListForUpdat.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "1":
                print("\nCurrent Selection : EDIT NAME\n")
                oldData = input("Enter a old name : ")
                newData = input("Enter a new name : ")
                with open(r"user.txt", "r") as file:
                    data = file.readlines()[int(userID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"user.txt", "a") as file:
                    file.write(data)
                file = open("user.txt", "r")
                lines = file.readlines()
                del lines[int(userID) - 101]
                newFile = open("user.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.userDict.update(
                    {
                        str(int(userID)): {
                            "name": newData,
                            "id": self.userDict[userID]["id"],
                            "address": self.userDict[userID]["address"],
                            "password": self.userDict[userID]["password"],
                        }
                    }
                )
            elif key_press == "2":
                print("\nCurrent Selection : EDIT ID\n")
                oldData = input("Enter a old id : ")
                newData = input("Enter a new id : ")
                with open(r"user.txt", "r") as file:
                    data = file.readlines()[int(userID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"user.txt", "a") as file:
                    file.write(data)
                file = open("user.txt", "r")
                lines = file.readlines()
                del lines[int(userID) - 101]
                newFile = open("user.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.userDict.update(
                    {
                        str(int(userID)): {
                            "name": newData,
                            "id": self.userDict[userID]["id"],
                            "address": self.userDict[userID]["address"],
                            "password": self.userDict[userID]["password"],
                        }
                    }
                )
            elif key_press == "3":
                print("\nCurrent Selection : EDIT PASSWORD\n")
                oldData = input("Enter a old password : ")
                newData = input("Enter a new password : ")
                with open(r"user.txt", "r") as file:
                    data = file.readlines()[int(userID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"user.txt", "a") as file:
                    file.write(data)
                file = open("user.txt", "r")
                lines = file.readlines()
                del lines[int(userID) - 101]
                newFile = open("user.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.userDict.update(
                    {
                        str(int(userID)): {
                            "name": newData,
                            "id": self.userDict[userID]["id"],
                            "address": self.userDict[userID]["address"],
                            "password": self.userDict[userID]["password"],
                        }
                    }
                )
            elif key_press == "4":
                print("\nCurrent Selection : EDIT ADDRESS\n")
                oldData = input("Enter a old address : ")
                newData = input("Enter a new address : ")
                with open(r"user.txt", "r") as file:
                    data = file.readlines()[int(userID) - 101]
                    data = data.replace(oldData, newData)
                with open(r"user.txt", "a") as file:
                    file.write(data)
                file = open("user.txt", "r")
                lines = file.readlines()
                del lines[int(userID) - 101]
                newFile = open("user.txt", "w+")
                for line in lines:
                    newFile.write(line)
                self.userDict.update(
                    {
                        str(int(userID)): {
                            "name": newData,
                            "id": self.userDict[userID]["id"],
                            "address": self.userDict[userID]["address"],
                            "password": self.userDict[userID]["password"],
                        }
                    }
                )
            elif key_press == "5":
                exit()

            print("✅✅✅ Update User Successfully ✅✅✅\n")
        else:
            print("❌❌❌ User ID Not Found ❌❌❌")
            return self.updateUser()


def main():
    try:
        myLibraryManagementSystem = LibraryManagementSystem(
            "listOfBooks.txt", "user.txt", "Osama"
        )
        print("\n---------- 📖 Welcome To Library Management System 📖 ---------\n")
        print("Plese enter a type of user:")
        print("1-Admin\n2-Users(students)")
        keyPressTypeUser = input("Press Key : ")
        if keyPressTypeUser == "1":
            admin = "Osama"
            password = "123"
            nameUser = input("Enter your name : ")
            passUser = input("Enter your password : ")
            if nameUser == admin and passUser == password:
                pressKeyListForAdmin = {
                    "D": "Display Books",
                    "A": "Add Book",
                    "S": "Show Issued Book",
                    "U": "Updite Book",
                    "X": "Delete Book",
                    "AS": "Add User",
                    "DS": "Display User",
                    "US": "Updite User",
                    "XS": "Delete User",
                    "Q": "Quit",
                }
                print("\nCurrent Selection : ADMIN\n")
                while True:
                    print(
                        f"\n---------- 📖 Welcome To {myLibraryManagementSystem.libraryName} Library Management System (ADMIN)📖 ---------\n"
                    )
                    for key, value in pressKeyListForAdmin.items():
                        print("Press", key, "To", value)
                    key_press = input("Press Key : ").lower()
                    if key_press == "a":
                        print("\nCurrent Selection : ADD BOOK\n")
                        myLibraryManagementSystem.addBooks()
                    elif key_press == "d":
                        print("\nCurrent Selection : DISPLAY BOOKS\n")
                        myLibraryManagementSystem.displayBooks()
                    elif key_press == "s":
                        print("\nCurrent Selection : SHOW ISSUED BOOKS\n")
                        myLibraryManagementSystem.showIssuedBooks()
                    elif key_press == "u":
                        print("\nCurrent Selection : UPDITE BOOK\n")
                        myLibraryManagementSystem.updateBook()
                    elif key_press == "x":
                        print("\nCurrent Selection : DELETE BOOK\n")
                        myLibraryManagementSystem.deleteBooks()

                    elif key_press == "xs":
                        print("\nCurrent Selection : DELETE USER\n")
                        myLibraryManagementSystem.deleteUser()
                    elif key_press == "us":
                        print("\nCurrent Selection : UPDITE USER\n")
                        myLibraryManagementSystem.updateUser()

                    elif key_press == "ds":
                        print("\nCurrent Selection : DISPLAY USER\n")
                        myLibraryManagementSystem.displayUser()

                    elif key_press == "as":
                        print("\nCurrent Selection : ADD USER\n")
                        myLibraryManagementSystem.addUser()

                    elif key_press == "q":
                        exit()
                    else:
                        continue
            else:
                print("❌❌❌ An error occurred during the login process ❌❌❌")
        elif keyPressTypeUser == "2":
            pressKeyListForUser = {
                "D": "Display Books",
                "I": "Request Book",
                "R": "Return Books",
                "Q": "Quit",
            }
            print("\nCurrent Selection : ADMIN\n")
            while True:
                print(
                    f"\n---------- 📖 Welcome To {myLibraryManagementSystem.libraryName} Library Management System (USERS-STUDENTS)📖 ---------\n"
                )
                for key, value in pressKeyListForUser.items():
                    print("Press", key, "To", value)
                key_press = input("Press Key : ").lower()
                if key_press == "d":
                    print("\nCurrent Selection : DISPLAY BOOKS\n")
                    myLibraryManagementSystem.displayBooks()

                elif key_press == "i":
                    print("\nCurrent Selection : REQUEST A BOOK\n")
                    myLibraryManagementSystem.issueBooks()

                elif key_press == "r":
                    print("\nCurrent Selection : RETURN BOOK\n")
                    myLibraryManagementSystem.returnBooks()
                elif key_press == "q":
                    exit()
                else:
                    continue
        else:
            print("❌❌❌ Error entry process ❌❌❌")

    except Exception as e:
        print("❌❌❌ Something went wrong. Please check ❌❌❌", e)


main()
