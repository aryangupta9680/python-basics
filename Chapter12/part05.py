# Find sequences of one uppercase letter followed by lowercase letters:

import re

text = input("Enter string to find capital letter followed by lowercase letters: ")

# Find all matches of one capital followed by one or more small letters
matches = re.findall(r'[A-Z][a-z]+', text)

print("Matches found:", matches)
