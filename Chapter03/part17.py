# Program to print the given number pattern with right alignment

n = int(input("Enter the number of rows: "))  # Take input from user

for i in range(1, n + 1):
    # Print leading spaces for right alignment
    for space in range(n - i):
        print("  ", end="")  # Two spaces for alignment

    # Print numbers from 1 to i
    for num in range(1, i + 1):
        print(num, end=" ")

    print()  # Move to next line
