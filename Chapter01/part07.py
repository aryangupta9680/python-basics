# Program to perform different identity operator operations on numbers

a = 10
b = 10
c = 20

print("a is b:", a is b)         # True, both refer to the same object/value
print("a is c:", a is c)         # False, different objects/values
print("a is not c:", a is not c) # True, a and c are not the same object
print("b is not c:", b is not c) # True, b and c are not the same object
