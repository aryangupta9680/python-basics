# Program to perform different Bitwise operators Operations on numbers

a = 10  # In binary: 1010
b = 4   # In binary: 0100

print("a =", a, "->", bin(a))
print("b =", b, "->", bin(b))

# Bitwise AND
print("a & b =", a & b, "->", bin(a & b))

# Bitwise OR
print("a | b =", a | b, "->", bin(a | b))

# Bitwise XOR
print("a ^ b =", a ^ b, "->", bin(a ^ b))

# Bitwise NOT
print("~a =", ~a, "->", bin(~a))

# Left Shift
print("a << 2 =", a << 2, "->", bin(a << 2))

# Right Shift
print("a >> 2 =", a >> 2, "->", bin(a >> 2))


# The bin() function in Python converts an integer number into its binary representation as a string.
num1 = 5
num2 = 18
num3 = 255

print(bin(num1))  # Output: 0b101   (5 in binary)
print(bin(num2))  # Output: 0b10010 (18 in binary)
print(bin(num3))  # Output: 0b11111111 (255 in binary)

# Note: The '0b' prefix means it's a binary literal in Python.
