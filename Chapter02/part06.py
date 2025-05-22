# Program to check if a year is a leap year or not

# Take input from the user and convert it to integer
year = int(input("Enter a year: "))

# Check if the year is a leap year
# Leap year if:
# 1. Year is divisible by 400, OR
# 2. Year is divisible by 4 but not by 100

if (year % 400 == 0):
    # If divisible by 400, it's a leap year
    print(f"{year} is a leap year.")
elif (year % 4 == 0) and (year % 100 != 0):
    # If divisible by 4 but not by 100, it's a leap year
    print(f"{year} is a leap year.")
else:
    # Otherwise, it's not a leap year
    print(f"{year} is not a leap year.")
