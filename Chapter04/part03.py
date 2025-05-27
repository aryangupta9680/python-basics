# Take input from user
user_string = input("Enter a string: ")

# Print the original string
print("You entered:", user_string)

# Use len() to find number of characters in string
print("Length of the string:", len(user_string))

# Use min() to find the smallest character (based on Unicode value)
print("Smallest character in the string:", min(user_string))

# Use max() to find the largest character (based on Unicode value)
print("Largest character in the string:", max(user_string))

# Accessing characters using index
print("First character (index 0):", user_string[0])
print("Last character (index -1):", user_string[-1])

print("Second last character (index -2):", user_string[-2])
print("Third character (index 2):", user_string[2])
