# Python program to find factorial of a number

# Take input from user
num = int(input("Enter a number: "))

# Initialize result variable
factorial = 1

# Check for negative numbers
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Multiply numbers from 1 to num
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}")
