# Program to find the largest among three numbers using nested if-else statements

# Input three numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Check if num1 is greater than or equal to num2
if num1 >= num2:
    # Now check if num1 is also greater than or equal to num3
    if num1 >= num3:
        # If both conditions are true, num1 is the largest
        largest = num1
    else:
        # Otherwise, num3 is the largest
        largest = num3
else:
    # num2 is greater than num1, so check if num2 is greater than or equal to num3
    if num2 >= num3:
        # If true, num2 is the largest
        largest = num2
    else:
        # Otherwise, num3 is the largest
        largest = num3

# Output the largest number
print("The largest number is:", largest)
