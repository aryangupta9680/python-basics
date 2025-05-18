# Program to swap two numbers using two methods

# Input from user
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

# Display before swapping
print("\nBefore Swapping:")
print("a =", a)
print("b =", b)

# Method 1: 
# temp = a
# a = b
# b = temp

# Display after Method 1
# print("\nAfter Swapping:")
# print("a =", a)
# print("b =", b)

# Method 2: 
a, b = b, a

# Display after Method 2
print("\nAfter Swapping:")
print("a =", a)
print("b =", b)


