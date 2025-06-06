# Program to handle divide by zero exception

# Take input from user
num = int(input("Enter a number to divide 100: "))

try:
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
