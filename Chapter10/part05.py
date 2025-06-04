# Multiple Inheritance: One class inherits from two parent classes

class Father:
    def input_father(self):
        self.father_name = input("Enter father's name: ")

class Mother:
    def input_mother(self):
        self.mother_name = input("Enter mother's name: ")

class Child(Father, Mother):
    def display_names(self):
        print("Father's Name:", self.father_name)
        print("Mother's Name:", self.mother_name)

# Create object
c = Child()
c.input_father()
c.input_mother()
c.display_names()
