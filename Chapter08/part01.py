# Function to swap two numbers
def swap(a, b):
    print("Before swapping: a =", a, ", b =", b)
    # Swapping logic
    a, b = b, a
    print("After swapping: a =", a, ", b =", b)

# Input from user
x = int(input("Enter first number (a): "))
y = int(input("Enter second number (b): "))

# Function call
swap(x, y)
