# Write a program to find the cumulative sum of elements of a list

# Input list of integers from user (space separated)
lst = input("Enter integers separated by space: ").split()

# Convert to integers
for i in range(len(lst)):
    lst[i] = int(lst[i])

cumulative_sum = []
current_sum = 0

# Calculate cumulative sum step by step
for num in lst:
    current_sum += num
    cumulative_sum.append(current_sum)

print("Cumulative sum list:", cumulative_sum)
