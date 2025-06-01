# Interchange first and last element of a list

# Take input list
lst = input("Enter list elements separated by space: ").split()

# Swap first and last elements if list length > 1
if len(lst) > 1:
    lst[0], lst[-1] = lst[-1], lst[0]

print("List after swapping first and last element:", lst)
