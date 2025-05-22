# Program to check if a number is an Armstrong number

n = int(input("Enter number: "))  # Read input number from user
temp = n                          # Store the original number to compare later
total = 0                         # Initialize sum of powered digits to zero
digits = len(str(n))              # Calculate number of digits in the number

while temp > 0:
    d = temp % 10                # Extract last digit
    total += d ** digits         # Add digit raised to the power of total digits
    temp //= 10                  # Remove last digit from temp

# Compare the sum with the original number
if total == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

