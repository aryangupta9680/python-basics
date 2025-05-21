# This code demonstrates usage of if-else statements with user input

# Example 1: Check if a number is positive or negative
num1 = int(input("Enter a number to check if it's positive or negative: "))
if num1 > 0:
    print("The number is positive.")
else:
    if num1 == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")


# Example 2: Check if a number is even or odd
num2 = int(input("\nEnter a number to check if it's even or odd: "))
if num2 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# Example 3: Check eligibility for voting
age = int(input("\nEnter your age to check voting eligibility: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

