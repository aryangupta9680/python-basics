# Replace whitespaces with underscores and vice versa:

import re

# Take input from user
text = input("Enter a string: ")

# Replace whitespace with underscore
replaced = re.sub(r"\s", "_", text)
print("Whitespaces replaced with underscores:", replaced)

# Replace underscore with whitespace
reversed_text = re.sub(r"_", " ", replaced)
print("Underscores replaced back to whitespaces:", reversed_text)
