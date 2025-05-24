# Example 1: Print numbers from 1 to n using while loop with else
n = int(input("Enter a positive number (n) to print numbers 1 to n using while-else: "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n") 
else:
    i = 1
    while i <= n:
        print(i, end=' ')
        i += 1
    else:
        print("\nLoop completed successfully.\n")


# Example 2: Check if all numbers from 1 to n are positive using while-else
n = int(input("Enter a positive number (n) to check positivity of numbers 1 to n using while-else: "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n") 
else:
    i = 1
    while i <= n:
        if i <= 0:
            print("Found a non-positive number:", i) 
            break
        i += 1
    else:
        print("All numbers from 1 to", n, "are positive.\n")


# Example 3: Print odd numbers from 1 to n using while loop with else
n = int(input("Enter a positive number (n) to print odd numbers 1 to n using while-else: "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    i = 1
    while i <= n:
        if i % 2 != 0:
            print(i, end=' ')
        i += 1
    else:
        print("\nFinished printing odd numbers.\n")