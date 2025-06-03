# Generate a random password of length 7 to 10 using ASCII 33–126

import random

def generate_password():
    password = ""
    length = random.randint(7, 10)  # Random length between 7 and 10
    for i in range(length):
        ch = chr(random.randint(33, 126))  # Random character from ASCII 33 to 126
        password += ch
    return password

# Call the function and display the password
print("Generated Password:", generate_password())
