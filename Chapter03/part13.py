# Program to print a triangle pattern 

# Takes number of rows for the increasing part
n = int(input("Enter the number of rows: "))

# Increasing pattern
for i in range(1, n + 1):
    for j in range(i):
        print("*", end='')  # print stars in the same line
    print('', end='\n')     # move to next line

# Decreasing pattern
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end='')  # print stars in the same line
    print('', end='\n')     # move to next line
