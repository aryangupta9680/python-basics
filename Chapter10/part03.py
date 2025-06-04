# Student Grade Calculator

class Grade:
    def __init__(self, marks):
        self.marks = marks

    def calculate(self):
        if self.marks < 0 or self.marks > 100:
            return "Invalid marks! Please enter marks between 0 and 100."
        elif self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"

m = int(input("Enter your marks: "))
g = Grade(m)
print("Your grade is:", g.calculate())
