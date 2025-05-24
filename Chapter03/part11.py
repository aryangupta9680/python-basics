# Program to print a right-angled triangle pattern of stars
# Example for input 4:
# *
# **
# ***
# ****


n = int(input("Enter number of rows: "))

# Outer loop for each row
for i in range(1, n + 1):
    # Inner loop to print stars in each row
    for j in range(i):
        print("*", end="")  # Print stars without newline
    print("\n", end="")     # Manually move to the next line
