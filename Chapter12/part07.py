# Search some literal strings in a string:

import re

# Take input from user
text = input("Enter a string: ")

# Search for any of the words: Python, Java, or C++
if re.search(r"Python|Java|C\+\+", text):
    print("Found one of the literal strings: Python, Java, or C++")
else:
    print("No matching literal strings found")
