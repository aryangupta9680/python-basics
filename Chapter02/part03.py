# This below code denotes if-elif-else statements

# Example 1: Check if a number is positive, negative, or zero
num = int(input("Enter a number to check if it's positive, negative, or zero: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# Example 2: Grade evaluation based on marks with input validation
marks = int(input("\nEnter your marks (0–100) to determine grade: "))
if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 75 and marks < 90:
    print("Grade: B")
elif marks >= 60 and marks < 75:
    print("Grade: C")
elif marks >= 40 and marks < 60:
    print("Grade: D")
elif marks >= 0 and marks < 40:
    print("Grade: F (Fail)")
else:
    print("Invalid marks entered. Marks should be between 0 and 100.")


# Example 3: Age-based category with validation for negative age
age = int(input("\nEnter your age to categorize: "))
if age >= 0 and age < 13:
    print("Category: Child")
elif age >= 13 and age < 20:
    print("Category: Teenager")
elif age >= 20 and age < 60:
    print("Category: Adult")
elif age >= 60:
    print("Category: Senior Citizen")
else:
    print("Invalid age entered. Age cannot be negative.")
