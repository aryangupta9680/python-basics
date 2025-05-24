# Program to print the given pattern using print

# The user inputs the maximum number of rows for the top half of the pattern
n = int(input("Enter the number of rows for the top half: "))

# Print the top half of the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")  # print numbers in a row separated by space, no newline yet
    print()  # move to the next line

# Print the bottom half of the pattern
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")  # print numbers in descending rows
    print()  # next line
