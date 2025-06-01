# Write a program that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of the values entered by the user (except for the 0) in order from smallest to largest, with one value appearing on each line.

# Read integers until 0, then print them sorted except 0

numbers = []

while True:
    val = input("Enter an integer (0 to stop): ")
    if val == '0':
        break
    numbers.append(int(val))

# Sort the numbers
numbers.sort()

# Print each number on a new line
print("Values entered (sorted):")
for num in numbers:
    print(num)
