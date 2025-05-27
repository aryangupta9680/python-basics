# String Comparison and String Methods in Python

# Take two strings as input from the user
S1 = input("Enter first string S1: ")
S2 = input("Enter second string S2: ")

# String comparison using operators
print("\nString Comparison Results:")
print("S1 == S2:", S1 == S2)    # Check if strings are equal
print("S1 != S2:", S1 != S2)    # Check if strings are not equal
print("S1 > S2:", S1 > S2)      # Check if S1 is greater than S2 
print("S1 < S2:", S1 < S2)      # Check if S1 is less than S2 

# Using format() method with positional arguments
print("\nUsing format() with positional arguments:")
print("{} plus {} equals {}".format(4, 5, 'Nine'))
print("{1} plus {0} equals {2}".format(4, 5, 'Nine'))

# Using format() method with keyword arguments
age = input("\nEnter your age: ")
print("I am {0} years old. I love to work on {PC} laptop.".format(age, PC="APPLE"))

# Using split() method
languages = input("\nEnter some programming languages separated by space: ")
lang_list = languages.split()  # split string into list by spaces
print("List of languages:", lang_list)
