
"""Modular Exponentiation (Power in Modular Arithmetic)"""

# bitwise Operators
def power(x, y):

    result = 1
    while y > 0:

        if y&1 != 0:
            result = result*x

        y = y >> 1
        x *= x
    return result

print(power(2, 3))
