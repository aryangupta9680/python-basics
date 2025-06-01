# Write a program to find the maximum and minimum K elements in a tuple

# Take input as a string (numbers only)
s = input("Enter tuple elements separated by commas or spaces (numbers only): ")

# Replace commas with spaces, then split by whitespace
elements = s.replace(',', ' ').split()

# Convert to integers
nums = []
for num in elements:
    nums.append(int(num))

k = int(input("Enter K: "))

# Sort the list
nums.sort()

# Print minimum K elements and maximum K elements
print("Minimum", k, "elements:", nums[:k])
print("Maximum", k, "elements:", nums[-k:])

