# Program to demonstrate string operators and slicing with user input

# Take input from user
text = input("Enter a string (length should be at least 5): ")

# Check if length is enough for slicing
if len(text) >= 5:
    # Safe to slice from index 2 to 4 (5 is exclusive)
    print("\nSlicing:", text[2:5])  # Characters at indices 2, 3, 4
else:
    print("Error: String length should be at least 5 for this slicing.")

# 2. Slicing with step size (every second character)
print("Characters from start to end with step 2:", text[0:len(text):2])

# 3. Print entire string using slicing
print("Entire string using slicing:", text[::])

# 4. Reverse the string
print("Reversed string:", text[::-1])

# 5. Reverse string from last to first (excluding first character)
print("Reverse string excluding first character:", text[-1:0:-1])

# 6. Exclude last character
print("String excluding last character:", text[:-1])

# 7. Concatenation (+ operator)
s1 = input("\nEnter first string to concatenate: ")
s2 = input("Enter second string to concatenate: ")
print("Concatenated string:", s1 + s2)

# 8. Repetition (* operator)
repeat = int(input("\nEnter how many times to repeat a word: "))
word = input("Enter the word to repeat: ")
print("Repeated string:", (word + " ") * repeat)  # Adds a space after each repetition

# 9. 'in' and 'not in' operator
main_text = input("\nEnter a sentence: ")
sub_text = input("Enter a word to search in the sentence: ")
print("Is the word in the sentence?", sub_text in main_text)
print("Is the word not in the sentence?", sub_text not in main_text)
