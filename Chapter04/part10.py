# Program to create, concatenate, and print strings
# Also accesses a substring from a given string

# Take two string inputs from the user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Concatenate the two strings
combined = str1 + " " + str2

# Print the concatenated string
print("Concatenated String:", combined)

# Access and print a substring from the first string
substring = str1[1:4]
print("Substring from first string (index 1 to 3):", substring)
