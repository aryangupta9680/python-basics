# Write a program to filter even values from a list using lambda function.

# Take space-separated input from user and convert each to integer
numbers = input("Enter numbers separated by space: ").split()
nums = []  # Create empty list

for val in numbers:
    nums.append(int(val))  # Convert each to integer and add to list

# Use lambda to filter even numbers
even_nums = list(filter(lambda x: x % 2 == 0, nums))

# Display result
print("Even numbers:", even_nums)
