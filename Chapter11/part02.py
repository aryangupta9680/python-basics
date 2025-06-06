# Program to handle IndexError exception

my_list = [10, 20, 30]
index = int(input("Enter index to access (0 to 2): "))

try:
    print("Value at index:", my_list[index])
except IndexError:
    print("Invalid index! List index out of range.")
