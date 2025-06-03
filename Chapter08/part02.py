# Function to perform arithmetic operations
def arithmetic(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Not possible (dividing by 0)")

# Input from user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Function call
arithmetic(x, y)
