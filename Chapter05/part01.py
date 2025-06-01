# Program to demonstrate basic list operations in Python

# Take input from the user and create a list
user_input = input("Enter numbers separated by spaces: ")
numbers = user_input.split()              # split input string into list elements
numbers = [int(num) for num in numbers]   # convert list of strings to integers

# Print the original list
print("Original list:", numbers)

# Important list operations
print("Length of list:", len(numbers))         # find length
print("First element:", numbers[0])            # access first element
print("Last element:", numbers[-1])            # access last element
print("Sorted list:", sorted(numbers))         # sort list (without modifying original)
numbers.append(100)                            # append an element
print("List after appending 100:", numbers)
numbers.remove(numbers[0])                     # remove first element
print("List after removing first element:", numbers)

