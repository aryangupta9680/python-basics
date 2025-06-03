# Function to find the median of three numbers
def find_median(a, b, c):
    if (a > b and a < c) or (a > c and a < b):
        return a
    elif (b > a and b < c) or (b > c and b < a):
        return b
    else:
        return c

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Function call and display result
median = find_median(num1, num2, num3)
print("Median value is:", median)
