# Demonstrating string immutability in Python

# Take input from the user
Str1 = input("Enter a string: ")

# Try to change the first character of the string
# This will raise a TypeError because strings are immutable
Str1[0] = "U"

# This line will not be executed due to the error above
print("Modified string:", Str1)
