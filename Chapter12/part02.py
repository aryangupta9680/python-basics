# Match a string that has an 'a' followed by zero or more 'b's:

import re

text = input("Enter string (a followed by zero or more b's): ")

# Pattern: 'a' followed by zero or more 'b's
if re.match(r'^ab*$', text):
    print("Match found!")
else:
    print("No match.")
