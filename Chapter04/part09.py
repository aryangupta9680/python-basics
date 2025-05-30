# Program to demonstrate stripping unwanted whitespace characters and string formatting

# Take string input from user (including spaces)
user_str = input("Enter a string with extra spaces or tabs: ")

# Show original string with repr() to make spaces/tabs visible
print("Original string:", repr(user_str))

# Remove leading whitespace characters
left_stripped = user_str.lstrip()
print("After lstrip (leading spaces removed):", repr(left_stripped))

# Remove trailing whitespace characters
right_stripped = user_str.rstrip()
print("After rstrip (trailing spaces removed):", repr(right_stripped))

# Remove leading and trailing whitespace characters
fully_stripped = user_str.strip()
print("After strip (both ends removed):", repr(fully_stripped))

# Formatting the stripped string by centering it in a field of width 20
centered = fully_stripped.center(20)
print("Centered string (width 20):", repr(centered))

# Left justify the stripped string in width 20
left_justified = fully_stripped.ljust(20)
print("Left justified (width 20):", repr(left_justified))

# Right justify the stripped string in width 20
right_justified = fully_stripped.rjust(20)
print("Right justified (width 20):", repr(right_justified))
