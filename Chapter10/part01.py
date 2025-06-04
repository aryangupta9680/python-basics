# Program to demonstrate constructor and destructor

class Book:
    def __init__(self, title):  # Constructor
        self.title = title
        print(f"Book '{self.title}' has been issued.")

    def __del__(self):  # Destructor
        print(f"Book '{self.title}' has been returned.")

# Take input from user
title = input("Enter the book title: ")
b = Book(title)

# Delete the object to trigger destructor
del b
