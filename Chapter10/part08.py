# Hybrid Inheritance: Combination of multiple and hierarchical inheritance

class Person:
    def input_name(self):
        self.name = input("Enter person's name: ")

class Student(Person):
    def input_roll(self):
        self.roll = input("Enter roll number: ")

class Teacher(Person):
    def input_subject(self):
        self.subject = input("Enter subject taught: ")

class TeachingAssistant(Student, Teacher):
    def display(self):
        print("Name:", self.name)
        print("Roll No.:", self.roll)
        print("Subject:", self.subject)

# Create object
t = TeachingAssistant()
t.input_name()
t.input_roll()
t.input_subject()
t.display()
