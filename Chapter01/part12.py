# Program to calculate the volume of a sphere

# Input radius from user
r = float(input("Enter the radius of the sphere: "))

# Assume pi
pi = 3.14

# Calculate volume of sphere: (4/3) * pi * r^3
volume = (4/3) * pi * (r ** 3)

# Display the result
print("Volume of the sphere with radius", r, "is:", volume)
