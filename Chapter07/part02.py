# Create dictionary from keys and values entered by user

keys = input("Enter keys (space-separated): ").split()
values = input("Enter values (space-separated): ").split()

# Combine using zip
my_dict = dict(zip(keys, values))

print("\nCreated Dictionary:")
print(my_dict)
