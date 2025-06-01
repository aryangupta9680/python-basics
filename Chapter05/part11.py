# Read integers until blank line, then print negatives, zeros, positives

negatives = []
zeros = []
positives = []

print("Enter integers one by one (blank line to stop):")

while True:
    val = input()
    if val == '':
        break
    num = int(val)
    if num < 0:
        negatives.append(num)
    elif num == 0:
        zeros.append(num)
    else:
        positives.append(num)

# Print negatives, zeros, and positives in order
for n in negatives:
    print(n)
for z in zeros:
    print(z)
for p in positives:
    print(p)
