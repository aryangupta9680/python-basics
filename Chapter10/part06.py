# Multilevel Inheritance: Derived class inherits from a class which is also a derived class

class Grandfather:
    def input_grandfather(self):
        self.grandfather_name = input("Enter grandfather's name: ")

class Father(Grandfather):
    def input_father(self):
        self.father_name = input("Enter father's name: ")

class Child(Father):
    def display_names(self):
        print("Grandfather:", self.grandfather_name)
        print("Father:", self.father_name)

# Create object
c = Child()
c.input_grandfather()
c.input_father()
c.display_names()
