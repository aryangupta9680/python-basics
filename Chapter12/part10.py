# Write a Program to validate a 10-digit mobile number

import re

# Take input from user
mobile = input("Enter a 10-digit mobile number: ")

# Check if it is a valid 10-digit number starting with 6-9
if re.match(r"^[6-9]\d{9}$", mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
