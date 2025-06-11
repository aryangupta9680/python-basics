# Match a word at the beginning of a string:

import re

# Take input from user
text = input("Enter a string: ")

# Check if the string starts with the word "Hello"
if re.match(r"Hello", text):
    print("The string starts with 'Hello'")
else:
    print("The string does not start with 'Hello'")
