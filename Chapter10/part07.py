# Hierarchical Inheritance: Multiple classes inherit from one parent class

class Parent:
    def input_parent(self):
        self.parent_name = input("Enter parent name: ")

class Child1(Parent):
    def show1(self):
        print("Child1's Parent:", self.parent_name)

class Child2(Parent):
    def show2(self):
        print("Child2's Parent:", self.parent_name)

# Create objects
c1 = Child1()
c2 = Child2()
c1.input_parent()
c1.show1()

c2.input_parent()
c2.show2()
