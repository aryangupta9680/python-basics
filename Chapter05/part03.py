# Find even numbers from a list

# Take space-separated integers input from user
lst = input("Enter numbers separated by space: ").split()

# Convert to integers
lst = [int(x) for x in lst]

# Find even numbers using list comprehension
even_nums = [x for x in lst if x % 2 == 0]

print("Even numbers:", even_nums)
