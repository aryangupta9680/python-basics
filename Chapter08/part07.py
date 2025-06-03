# Find the sum of elements in a list using a lambda function

# Take space-separated numbers from user
numbers = input("Enter numbers separated by space: ").split()

# Convert strings to integers
nums = []
for num in numbers:
    nums.append(int(num))

# Lambda function to add two numbers
add = lambda x, y: x + y

# Initialize total sum to 0
total = 0

# Use lambda to add each number to total
for n in nums:
    total = add(total, n)

# Print the sum
print("Sum of elements:", total)
