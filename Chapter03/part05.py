# Example 1: Print numbers from 1 to n using for loop with else
n = int(input("Enter a positive number (n) to print numbers 1 to n using for-else: "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    for i in range(1, n + 1):
        print(i, end=' ')
    else:
        print("\nLoop completed successfully.\n")


# Example 2: Check if all numbers from 1 to n are positive using for-else
n = int(input("Enter a positive number (n) to check positivity of numbers 1 to n using for-else: "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    for i in range(1, n + 1):
        if i <= 0:
            print("Found a non-positive number:", i)
            break
    else:
        print("All numbers from 1 to", n, "are positive.\n")


# Example 3: Print even numbers from 1 to n using for loop with else
n = int(input("Enter a positive number (n) to print even numbers 1 to n using for-else: "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, end=' ')
    else:
        print("\nFinished printing even numbers.\n")
