# Remove all whitespaces from a string:

import re

# Take input from user
text = input("Enter a string: ")

# Remove all whitespace characters (spaces, tabs, newlines)
no_space = re.sub(r"\s+", "", text)
print("String without whitespaces:", no_space)

