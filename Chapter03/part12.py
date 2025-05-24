# Program to print inverted star pattern 
# Example for input 4:
# ****
# ***
# **
# *

# Take number of rows as input from user
rows = int(input("Enter number of rows: "))

# Outer loop for each row
for i in range(rows, 0, -1):
    # Inner loop to print stars
    for j in range(i):
        print("*", end="")  # Print stars on the same line
    print(end="\n")         # Move to the next line after each row
