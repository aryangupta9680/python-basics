# Operator Precedence and Associativity in Python
# -----------------------------------------------
# Precedence | Operators                                     | Description                                                                 | Associativity
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 1          | ()                                            | Parentheses                                                                 | Left to Right
# 2          | x[index], x[index:index]                      | Subscription, slicing                                                       | Left to Right
# 3          | await x                                       | Await expression                                                            | N/A
# 4          | **                                            | Exponentiation                                                              | Right to Left
# 5          | +x, -x, ~x                                    | Unary plus, unary minus, bitwise NOT                                        | Right to Left
# 6          | *, @, /, //, %                                | Multiplication, matrix multiplication, division, floor division, remainder  | Left to Right
# 7          | +, -                                          | Addition and subtraction                                                    | Left to Right
# 8          | <<, >>                                        | Bitwise shifts                                                              | Left to Right
# 9          | &                                             | Bitwise AND                                                                 | Left to Right
# 10         | ^                                             | Bitwise XOR                                                                 | Left to Right
# 11         | |                                             | Bitwise OR                                                                  | Left to Right
# 12         | <, <=, >, >=, !=, ==, in, not in, is, is not  | Comparisons, membership and identity tests                                  | Left to Right
# 13         | not x                                         | Boolean NOT                                                                 | Right to Left
# 14         | and                                           | Boolean AND                                                                 | Left to Right
# 15         | or                                            | Boolean OR                                                                  | Left to Right
# 16         | :=                                            | Assignment expression (walrus)                                              | Right to Left

# Notes:
# Parentheses () have the highest precedence and can override any order.
# Associativity defines the order of evaluation for operators of the same precedence:
# Left to Right means operators are evaluated from left operand to right operand.
# Right to Left means operators are evaluated from right operand to left operand.
# Some operators like 'await' and 'lambda' have no associativity since they cannot chain.


# Operator Precedence and Associativity Example

# Expression:
result = 3 + 4 * 2 / (1 - 5) ** 2 ** 3

# Step-by-step evaluation order (due to precedence and associativity):
# 1. Parentheses: (1 - 5) → -4
# 2. Exponentiation (right to left associativity): 2 ** 3 → 8
# 3. Exponentiation again: (-4) ** 8 → 65536
# 4. Multiplication: 4 * 2 → 8
# 5. Division: 8 / 65536 → 0.00012207 approx
# 6. Addition: 3 + 0.00012207 → 3.00012207 approx

print(result)  # Output: 3.0001220703125
