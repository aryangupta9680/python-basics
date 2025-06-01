# Check if a string is a palindrome

text = input("Enter a string: ")

# Reverse the string and compare with original
if text == text[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")
