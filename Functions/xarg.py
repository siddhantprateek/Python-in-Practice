# An asterisk (*) is placed before the variable name that holds the values of all nonkeyword variable arguments.
# This tuple remains empty if no additional arguments are specified during the function call.

def multiply(*numbers):   # (*number) it pack all item into a list
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
