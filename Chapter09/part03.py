# Program to print Fibonacci series up to n terms using recursion

def fibonacci(n):
    if n == 0:
        return 0  # base case
    elif n == 1:
        return 1  # base case
    return fibonacci(n - 1) + fibonacci(n - 2)  # recursive call

# Taking input from user
terms = int(input("Enter number of terms in Fibonacci series: "))

print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=" ")
