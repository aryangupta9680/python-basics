# Program to calculate the sum and average of digits in a registration number

# Take input from the user
reg_no = input("Enter your registration number: ")

# Initialize sum and count
digit_sum = 0
count = 0

# Loop through each character in the input
for ch in reg_no:
    if ch.isdigit():         # Check if the character is a digit
        digit_sum += int(ch) # Add the digit to the sum
        count += 1           # Increase the count of digits

# Check if any digits were found
if count > 0:
    avg = digit_sum / count
    print("Sum of digits:", digit_sum)
    print("Average of digits:", avg)
else:
    print("No digits found in the registration number.")
