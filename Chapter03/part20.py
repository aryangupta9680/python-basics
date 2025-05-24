# Program to print the pyramid number pattern:
# Example for 5 rows:
#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

# Take input for number of rows
n = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, n+1):
    # Print leading spaces to center the pyramid
    print("  " * (n - i), end="")  # two spaces per unit for alignment
    
    # Print increasing numbers from 1 to i
    for j in range(1, i+1):
        print(j, end=" ")
    
    # Print decreasing numbers from i-1 down to 1
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    
    # Move to the next line after each row
    print()
