# Program to print the pattern:
# For input n=5, prints:
#         5
#       5 4
#     5 4 3
#   5 4 3 2
# 5 4 3 2 1


# Take input from user for number of rows
n = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, n + 1):
    # Print spaces before numbers to align the pattern
    print("  " * (n - i), end="")  # Two spaces for each indentation

    # Print numbers starting from n down to (n - i + 1)
    for j in range(n, n - i, -1):
        print(j, end=" ")

    # Move to next line after each row
    print()
