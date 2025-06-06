# Program to handle ValueError exception

# Take input and convert to integer
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
