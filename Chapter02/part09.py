# Program to print grade based on student's marks using multiple if statements

# Take input from the user and convert it to integer
marks = int(input("Enter the student's marks: "))

# Check for invalid input
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")

# Check if the marks are greater than or equal to 80
if marks >= 80 and marks <= 100:
    print("Grade: Excellent")

# Check if the marks are between 65 (inclusive) and 80 (exclusive)
if marks >= 65 and marks < 80:
    print("Grade: Good")

# Check if the marks are between 50 (inclusive) and 65 (exclusive)
if marks >= 50 and marks < 65:
    print("Grade: Pass")

# Check if the marks are less than 50 and greater than or equal to 0
if marks >= 0 and marks < 50:
    print("Grade: Fail")

