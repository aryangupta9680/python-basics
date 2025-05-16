# Program to perform different Arithmetic Operations on numbers

# Input two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nArithmetic Operations:")

# Addition
addition = a + b
print("Addition (a + b) =", addition)

# Subtraction
subtraction = a - b
print("Subtraction (a - b) =", subtraction)

# Multiplication
multiplication = a * b
print("Multiplication (a * b) =", multiplication)

# Division
if b != 0:
    division = a / b
    print("Division (a / b) =", division)
else:
    print("Division (a / b) = Division by zero not allowed")

# Floor Division
if b != 0:
    floor_division = a // b
    print("Floor Division (a // b) =", floor_division)
else:
    print("Floor Division (a // b) = Division by zero not allowed")

# Modulus
if b != 0:
    modulus = a % b
    print("Modulus (a % b) =", modulus)
else:
    print("Modulus (a % b) = Division by zero not allowed")

# Exponentiation
exponentiation = a ** b
print("Exponentiation (a ** b) =", exponentiation)
