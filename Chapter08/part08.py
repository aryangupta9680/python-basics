# Find the smaller number between two numbers using lambda function.

# Take input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Lambda function to find the smaller number
smaller = lambda x, y: x if x < y else y

# Call the lambda and print result
print("Smaller number is:", smaller(a, b))
