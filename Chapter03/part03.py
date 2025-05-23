# Example 1: Using break in for loop
n = int(input("Enter a positive number (n) to print numbers from 1 to n, but stop at 5: "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    print("Numbers from 1 to", n, "but stopping at 5 (break example):")
    for i in range(1, n + 1):
        if i > 5:  # Stop loop when i exceeds 5
            break
        print(i, end=' ')
    print("\n")


# Example 2: Using continue in for loop
n = int(input("Enter a positive number (n) to print odd numbers from 1 to n (continue example): "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    print("Odd numbers from 1 to", n, ":")
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue  # Skip even numbers
        print(i, end=' ')
    print("\n")


# Example 3: Using pass in for loop
n = int(input("Enter a positive number (n) to print numbers from 1 to n (pass example): "))
if n <= 0:
    print("Invalid input! Enter a positive number greater than 0.\n")
else:
    print("Numbers from 1 to", n, "with pass statement (no effect):")
    for i in range(1, n + 1):
        if i % 2 == 0:
            pass  # pass does nothing here
        print(i, end=' ')
    print("\n")
