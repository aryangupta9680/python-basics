# Program to check if a number is a palindrome

# Take input from user and convert it to string
num = input("Enter a number: ")

# Check if the number string is the same when reversed
if num == num[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
