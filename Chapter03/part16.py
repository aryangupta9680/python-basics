# Program to print a right-aligned triangle pattern of stars

n = int(input("Enter the number of rows: "))  # Number of rows in the pattern

for i in range(1, n + 1):
    # Print spaces to right-align stars
    for space in range(n - i):
        print("  ", end="")  # Two spaces to align with star + space
    
    # Print stars separated by space
    for star in range(i):
        print("* ", end="")
    
    # Move to the next line
    print()
