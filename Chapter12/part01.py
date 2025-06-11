# Match a string that contains only upper/lowercase letters, numbers, and underscores:

import re

# Input from user
text = input("Enter string (letters, numbers, underscores only): ")

# Check using regular expression
if re.match(r'^[A-Za-z0-9_]+$', text):
    print("Valid string!")
else:
    print("Invalid string!")
