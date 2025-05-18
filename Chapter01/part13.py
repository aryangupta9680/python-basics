# Easy program to show type casting with value, type, and id
num_int = 10
num_float = 15.75
text_str = "123"
flag_bool = True
comp_num = 3 + 4j

print("Original Values:")
# Integer
print(num_int)
print(type(num_int))
print(id(num_int))

# Float
print(num_float)
print(type(num_float))
print(id(num_float))

# String
print(text_str)
print(type(text_str))
print(id(text_str))

# Boolean (a subclass of int in Python)
print(flag_bool)
print(type(flag_bool))
print(id(flag_bool))

# Complex
print(comp_num)
print(type(comp_num))
print(id(comp_num))

print("-" * 40)

print("\nCasting from int:")
print(float(num_int))
print(type(float(num_int)))

print(str(num_int))
print(type(str(num_int)))

print(bool(num_int))
print(type(bool(num_int)))

print(complex(num_int))
print(type(complex(num_int)))

print("-" * 40)

print("\nCasting from float:")
print(int(num_float))
print(type(int(num_float)))

print(str(num_float))
print(type(str(num_float)))

print(bool(num_float))
print(type(bool(num_float)))

print(complex(num_float))
print(type(complex(num_float)))

print("-" * 40)

print("\nCasting from str:")
print(int(text_str))
print(type(int(text_str)))

print(float(text_str))
print(type(float(text_str)))

print(bool(text_str))
print(type(bool(text_str)))

print(complex(text_str))
print(type(complex(text_str)))

# Note: If text_str were "123abc" or "abc", int(text_str) and float(text_str) would raise a ValueError

print("-" * 40)

print("\nCasting from bool:")
print(int(flag_bool))
print(type(int(flag_bool)))

print(float(flag_bool))
print(type(float(flag_bool)))

print(str(flag_bool))
print(type(str(flag_bool)))

print(complex(flag_bool))
print(type(complex(flag_bool)))

print("-" * 40)

print("\nCasting from complex:")
print(str(comp_num))
print(type(str(comp_num)))

# Note: complex to int, float, bool cast is invalid and not shown.
print("-" * 40)
