# Program to test different string properties using string methods

# Take string input from user
s = input("Enter a string: ")

# Check if string is alphanumeric (letters and numbers, no spaces)
print("Is alphanumeric?", s.isalnum())

# Check if string contains only alphabets
print("Is alphabetic?", s.isalpha())

# Check if string contains only digits
print("Is digit?", s.isdigit())

# Check if all characters are lowercase
print("Is lowercase?", s.islower())

# Check if all characters are uppercase
print("Is uppercase?", s.isupper())

# Check if string contains only whitespace characters
print("Is whitespace?", s.isspace())
