# Take input from the user for number of rows
n = int(input("Enter number of rows: "))

# Loop through each row from 1 to n
for i in range(1, n + 1):
    # For each row, print numbers from 1 to i with space after each number
    for j in range(1, i + 1):
        print(j, end=" ")  # Print number and a space, no newline
    print()  # Print newline after each row
