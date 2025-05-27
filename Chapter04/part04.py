# Take input string from the user
S = input("Enter a string: ")

# Traversing string using a for loop
print("Using for loop:")
for ch in S:
    print(ch, end="")
print()  # for newline


# Traversing string using a while loop
print("Using while loop:")
index = 0
while index < len(S):
    print(S[index], end="")
    index += 1
print()  # for newline
