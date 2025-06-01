# Write a program to demonstrate various tuple operations in python.

# Take input as a string
s = input("Enter tuple elements separated by commas or spaces: ")

# Replace commas with spaces, then split by whitespace
elements = s.replace(',', ' ').split()

# Convert to tuple
t = tuple(elements)

print("Tuple:", t)
print("Length:", len(t))
print("Tuple repeated twice:", t * 2)
print("First element:", t[0])
print("Last element:", t[-1])
print("Slice first 3 elements:", t[:3])
print("Is 'a' in tuple?", 'a' in t)
