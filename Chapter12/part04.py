# Match a string that has an 'a' followed by exactly three 'b's:

import re

text = input("Enter string (a followed by exactly three b's): ")

# Pattern: 'a' followed by exactly 3 b's
if re.match(r'^ab{3}$', text):
    print("Match found!")
else:
    print("No match.")
