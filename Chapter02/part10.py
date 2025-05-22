# Program to calculate scholarship based on family income (in rupees) and academic percentage

# Scholarship Criteria:
# If family income <= ₹30,00,000 and percentage >= 90%, scholarship = Full tuition waiver
# If family income <= ₹30,00,000 and 75% < percentage < 90%, scholarship = 50% tuition waiver
# If family income between ₹30,00,000 and ₹60,00,000 and percentage >= 85%, scholarship = 25% tuition waiver
# If family income > ₹60,00,000 and percentage >= 95%, scholarship = 10% tuition waiver
# Otherwise, no scholarship

# This program also checks for invalid inputs (negative values or percentage > 100)

# Input family income and academic percentage
income = float(input("Enter annual family income in rupees: "))
percentage = float(input("Enter academic percentage: "))

# Initialize scholarship variable
scholarship = "No scholarship"

# Check for invalid input values
if income < 0:
    print("Invalid input! Family income cannot be negative.")
elif percentage < 0 or percentage > 100:
    print("Invalid input! Percentage must be between 0 and 100.")
else:
    # Check conditions for scholarship
    if income <= 3000000:  # ₹30,00,000
        if percentage >= 90:
            scholarship = "Full tuition waiver"
        elif 75 < percentage < 90:
            scholarship = "50% tuition waiver"
    elif 3000000 < income <= 6000000:  # ₹30,00,000 to ₹60,00,000
        if percentage >= 85:
            scholarship = "25% tuition waiver"
    elif income > 6000000:  # Greater than ₹60,00,000
        if percentage >= 95:
            scholarship = "10% tuition waiver"

    # Print scholarship awarded
    print("Scholarship awarded:", scholarship)

