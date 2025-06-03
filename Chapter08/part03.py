# Function to calculate diameter and area of circle
def circle(radius):
    diameter = 2 * radius
    area = 3.14 * radius * radius
    print("Diameter of circle:", diameter)
    print("Area of circle:", area)

# Input from user
r = float(input("Enter radius of circle: "))

# Function call
circle(r)
