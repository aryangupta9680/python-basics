# Write a program to replace list’s item with new value if found

# Input list from user (space separated values)
lst = input("Enter list items separated by space: ").split()

# Input the item to replace and the new value
old_value = input("Enter the item to replace: ")
new_value = input("Enter the new value: ")

# Replace old_value with new_value wherever found in list
for i in range(len(lst)):
    if lst[i] == old_value:
        lst[i] = new_value

print("Updated list:", lst)

