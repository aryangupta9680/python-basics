# Count unique characters in a string

text = input("Enter a string: ")
unique_chars = {}

for char in text:
    if char != ' ':
        unique_chars[char] = 1

print("\nNumber of unique characters:", len(unique_chars))
