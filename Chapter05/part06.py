# Check if all elements are unique or not

# Take input list
lst = input("Enter list elements separated by space: ").split()

# Check uniqueness by comparing length of list and set
if len(lst) == len(set(lst)):
    print("All elements are unique.")
else:
    print("There are duplicate elements.")
