# Generate squares from 1 to N

N = int(input("Enter a number: "))
squares = {}

for i in range(1, N + 1):
    squares[i] = i * i

print("\nNumber : Square")
print(squares)
