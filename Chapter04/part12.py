# Count letters, digits, and special symbols in a string

text = input("Enter any string: ")

letters = digits = symbols = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special Symbols:", symbols)
