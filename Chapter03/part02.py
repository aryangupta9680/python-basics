# Example 1: Print numbers from 1 to n
n = int(input("Enter a positive number (n) to print numbers from 1 to n: "))
if n <= 0:
    print("Invalid input! Please enter a positive number greater than 0.\n")
else:
    print("Numbers from 1 to", n, ":")
    for i in range(1, n + 1):
        print(i, end=' ')
    print("\n")


# Example 2: Print even numbers from 1 to n using if-else

# First Method
n = int(input("Enter a positive number to print even numbers: "))
if n <= 0:
    print("Invalid input! Please enter a positive number greater than 0.\n")
else:
    print("Even numbers from 1 to", n, ":")
    for i in range(1, n + 1):
        if i % 2 == 0:  # Check if number is even
            print(i, end=' ')
        else:
            pass
    print("\n")


# Second Method
n = int(input("Enter a positive number to print even numbers: "))
if n < 2:
    print("No even numbers to display.\n")
else:
    print("Even numbers from 1 to", n, ":")
    for i in range(2, n + 1, 2):
        print(i, end=' ')
    print("\n")


# Example 3: Print multiplication table of a number
num = int(input("Enter a number to print its multiplication table: "))
if num == 0:
    print("Multiplication table of 0 is always 0.\n")
else:
    print(f"Multiplication table of {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

