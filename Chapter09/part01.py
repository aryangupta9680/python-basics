# Program to find factorial of a number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1  # base case
    return n * factorial(n - 1)  # recursive call

# Taking input from user
num = int(input("Enter a number to find its factorial: "))
print("Factorial:", factorial(num))
