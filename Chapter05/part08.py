# Write a program to find the position of minimum and maximum elements of a list.

# Input list of integers from user (space separated)
lst = input("Enter integers separated by space: ").split()

# Convert to integers
for i in range(len(lst)):
    lst[i] = int(lst[i])

# Initialize min and max positions
min_pos = 0
max_pos = 0

# Iterate to find min and max index
for i in range(1, len(lst)):
    if lst[i] < lst[min_pos]:
        min_pos = i
    if lst[i] > lst[max_pos]:
        max_pos = i

print("Position of minimum element:", min_pos)
print("Position of maximum element:", max_pos)
