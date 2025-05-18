# Using sep to set item separators and end to control line endings

print("Python", "is", "fun", sep="-")        # Prints with '-' between words
print("Hello", end=" ")                      # Prints 'Hello' and stays on the same line with a space
print("World!")                              # Continues on the same line after 'Hello '
print("Apple", "Banana", "Cherry", sep=" | ", end=" -> ")  # Separate fruits with ' | ' and end with ' -> ' 
print("Fruit Basket")  # Continue printing on the same line after ' -> '
print("2025", "05", "15", sep="-", end="\n")  # Print date parts separated by '-' and end with newline
print("Date printed with hyphens.")  # Print a message on the next line

