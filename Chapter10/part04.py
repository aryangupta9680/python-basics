# Single Inheritance Example

class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):  # Inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()  # Inherited method
d.bark()   # Child class method
