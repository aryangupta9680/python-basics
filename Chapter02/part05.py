# Program to find the smaller number among two numbers

# Input: taking two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers using if-elif-else statements
if num1 < num2:
    # If first number is smaller
    print(f"The smaller number is {num1}")
elif num2 < num1:
    # If second number is smaller
    print(f"The smaller number is {num2}")
else:
    # If both numbers are equal
    print("Both numbers are equal.")
