# Example 1: Using break in while loop
n = int(input("Enter a positive number (n) to print numbers from 1 to n, but stop at 5 (while loop): "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    print("Numbers from 1 to", n, "but stopping at 5 (break example):")
    i = 1
    while i <= n:
        if i > 5:
            break
        print(i, end=' ')
        i += 1
    print("\n")


# Example 2: Using continue in while loop
n = int(input("Enter a positive number (n) to print odd numbers from 1 to n (continue example - while loop): "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    print("Odd numbers from 1 to", n, ":")
    i = 1
    while i <= n:
        if i % 2 == 0:
            i += 1
            continue  # Skip even numbers
        print(i, end=' ')
        i += 1
    print("\n")


# Example 3: Using pass in while loop
n = int(input("Enter a positive number (n) to print numbers from 1 to n (pass example - while loop): "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    print("Numbers from 1 to", n, "with pass statement (no effect):")
    i = 1
    while i <= n:
        if i % 2 == 0:
            pass  # pass does nothing here
        print(i, end=' ')
        i += 1
    print("\n")
