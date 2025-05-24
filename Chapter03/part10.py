# Program to print Fibonacci series up to n terms

# Take input from user for number of terms
n = int(input("Enter the number of terms: "))

# Initialize first two Fibonacci numbers
a, b = 0, 1

# Print Fibonacci series using a loop
for i in range(n):
    print(a, end=' ')
    # Update values of a and b
    a, b = b, a + b
