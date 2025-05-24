# Program to print prime numbers less than a given number

# Take input from user
n = int(input("Enter a number: "))

print(f"Prime numbers less than {n} are:")

# Loop through numbers from 2 to n-1
for num in range(2, n):
    is_prime = True  # Assume the number is prime

    # Check for factors from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False  # If divisible, it's not prime
            break  # Exit the loop early

    # If it is prime, print it
    if is_prime:
        print(num)
