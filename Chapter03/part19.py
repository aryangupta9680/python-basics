# Program to print a pyramid pattern of stars
# The pyramid has increasing odd number of stars per row
# Example for 5 rows:
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

# Take number of rows as input from the user
rows = int(input("Enter number of rows: "))

# Loop through each row
for i in range(rows):
    # Print spaces to center the stars
    print("  " * (rows - i - 1), end="")
    # Print stars: number of stars = 2*i + 1
    print("* " * (2 * i + 1))
