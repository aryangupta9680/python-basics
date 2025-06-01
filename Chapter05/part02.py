# Demonstrate various list operations

# Take space-separated input from user and convert to list of integers
lst = input("Enter list elements separated by space: ").split()

# Demonstrate some list operations
print("Original list:", lst)
print("Length of list:", len(lst))
print("First element:", lst[0])
print("Last element:", lst[-1])

lst.append("new")  # Add an element
print("After appending 'new':", lst)

lst.insert(1, "inserted")  # Insert at index 1
print("After inserting 'inserted' at index 1:", lst)

lst.remove("new")  # Remove element 'new'
print("After removing 'new':", lst)

lst.pop()  # Remove last element
print("After popping last element:", lst)
