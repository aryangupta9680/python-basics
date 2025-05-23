# Program 1: Print numbers from 1 to n using while loop with input validation
n = int(input("Enter a number to print 1 to n: "))
if n <= 0:
    print("Please enter a number greater than 0.")
else:
    i = 1
    print("Numbers from 1 to", n, ":")
    while i <= n:
        print(i, end=" ")
        i += 1
print("\n")  # Newline for separation


# Program 2: Print even numbers from 1 to n using while loop and if-else
n = int(input("Enter a number to print even numbers till n: "))
if n < 1:
    print("Please enter a number greater than or equal to 1.")
else:
    i = 1
    print("Even numbers from 1 to", n, ":")
    while i <= n:
        if i % 2 == 0:
            print(i, end=" ")
        else:
            pass  # Skips odd numbers
        i += 1
print("\n")


# Program 3: Calculate sum of first n natural numbers using while loop
n = int(input("Enter a number to calculate sum of first n natural numbers: "))
if n < 1:
    print("Please enter a positive number.")
else:
    i = 1
    total = 0
    while i <= n:
        total += i
        i += 1
    print("Sum of first", n, "natural numbers is:", total)


# Example 4: Calculate sum of first n natural numbers
n = int(input("Enter a positive number to calculate sum of first n natural numbers: "))
if n <= 0:
    print("Invalid input! Please enter a number greater than 0.")
else:
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Sum of first {n} natural numbers is: {total}")