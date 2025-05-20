# Explanation of format specifiers used in the code:
# format(value, format_spec) formats the value according to format_spec.
#
# 10       → width of the output field (total spaces).
# .2       → number of digits after the decimal point.
# f        → fixed-point decimal notation.
# e        → scientific notation.
# %        → percentage format (multiplies value by 100 and adds %).
# x        → hexadecimal integer.
# s        → string format.
# <        → left align.
# >        → right align.


# Additional format examples:
# 10.2f    → Format floating point number with precision 2 and width 10.
# <10.2f   → Left justify the floating point number within width 10.
# >10.2f   → Right justify the floating point number within width 10.
# 10x      → Format integer in hexadecimal with width 10.
# 20s      → Format string with width 20.
# 10.2%    → Format the number as a percentage with 2 decimals and width 10.


# Integer Formatting - Hexadecimal
print(format(20, "10x"))     # Format integer 20 as hex, width 10, right aligned by default
print(format(20, "<10x"))    # Format integer 20 as hex, width 10, left aligned

# Floating Point Formatting
print(format(10.345, "10.2f"))   # Float with width 10, 2 decimal places (rounded)
print(format(10, "10.2f"))       # Integer formatted as float with 2 decimals, width 10
print(format(10.32245, "10.2f")) # Float rounded to 2 decimals, width 10

# String Formatting
print(format("Hello World!", "25s"))  # String left justified with width 25 (default is left align)
print(format("HELLO WORLD!", ">20s")) # String right justified with width 20

# Percentage Formatting
print(format(0.31456, "10.2%"))  # Number as percentage: 31.46%, width 10
print(format(3.1, "10.2%"))      # Number as percentage: 310.00%, width 10
print(format(1.765, "10.2%"))    # Number as percentage: 176.50%, width 10

# Scientific Notation Formatting
print(format(31.2345, "10.2e"))   # Scientific notation with 2 decimals, width 10 (3.12e+01)
print(format(131.2345, "10.2e"))  # Scientific notation with 2 decimals, width 10 (1.31e+02)
