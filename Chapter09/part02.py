# Program to read values from user until blank line and display total using recursion

def read_and_sum():
    val = input("Enter a number (leave blank to stop): ")
    if val == "":
        return 0.0  # base case
    return float(val) + read_and_sum()  # recursive sum

print("Total sum:", read_and_sum())
