# Program to demonstrate the str class and string creation in Python

# Creating strings using the str() constructor
S1 = str()           # Creates an empty string using constructor
S2 = str("Hello")    # Creates a string object for "Hello"

# Alternative and more common way to create strings
S3 = ""              # Creates an empty string directly
S4 = "Hello"         # Equivalent to str("Hello")

# Taking input from user
user_input = input("Enter your name: ")  # Input is always taken as a string

# Creating a greeting message using str() constructor (correct but not necessary)
greeting1 = str("Welcome, " + user_input + "!")

# Creating a greeting message using direct string concatenation (simpler and preferred)
greeting2 = "Welcome, " + user_input + "!"

# Displaying both greeting messages
print("Using str() constructor:", greeting1)
print("Using direct concatenation (preferred):", greeting2)
