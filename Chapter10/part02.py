# Getters and Setters Example

class Student:
    def __init__(self):
        self._marks = 0  # Protected attribute

    def set_marks(self, m):  # Setter method
        self._marks = m

    def get_marks(self):  # Getter method
        return self._marks

s = Student()
m = int(input("Enter your marks: "))
s.set_marks(m)
print("Marks are:", s.get_marks())
