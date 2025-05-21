# Ask the user to enter a number for the day of the week
day_num = int(input("Enter a day number (1-7): "))

# Check which day the number represents and print the day name
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    # If the number is not between 1 and 7, show an error message
    print("Invalid input! Please enter a number between 1 and 7.")
