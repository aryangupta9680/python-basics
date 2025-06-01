# Write a program to turn every item of a list into its square

# Take space-separated numbers input
lst = input("Enter numbers separated by space: ").split()

# Convert to integers
lst = [int(x) for x in lst]

# Square each element using a loop
for i in range(len(lst)):
    lst[i] = lst[i] ** 2

print("List after squaring each element:", lst)


