# Program to handle TypeError exception

# Take user input
num = input("Enter a number: ")

try:
    result = num + 10  # invalid operation: string + int
    print("Result:", result)
except TypeError:
    print("Type Error! You can't add string and number directly.")
