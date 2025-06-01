# Write a program to find the size of a tuple

# Take input as a string
s = input("Enter tuple elements separated by commas or spaces: ")

# Replace commas with spaces, then split by whitespace
elements = s.replace(',', ' ').split()

# Convert to tuple
t = tuple(elements)

# Print size of the tuple
print("Size of tuple:", len(t))

