# Write a program to create a list of tuples from given list having number and its cube in each tuple

# Take input as a string (numbers only)
s = input("Enter numbers separated by commas or spaces: ")

# Replace commas with spaces, then split by whitespace
elements = s.replace(',', ' ').split()

# Create list of tuples (number, cube)
result = []
for num in elements:
    n = int(num)
    result.append((n, n**3))

print("List of tuples (number, cube):", result)

