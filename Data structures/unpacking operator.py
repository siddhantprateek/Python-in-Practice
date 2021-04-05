number = [1, 2, 3]
# to unpack it we prefix it with asterisk
# / *number

print(*number)

# or
values = list(range(10))
# we can unpack any iterable it does not have to be a list
print(*values)
# range is iterable coverted into a list by square bracket
values = [*range(20)]
print(values)

# we can unpack multiple list into single list
# f = [1,2] s=[3]
# values = [ *f, *s, *"string"]

# we can unpack a dictionary we need to prefix it with double asterisk
first = {"x": 1}
second = {"x": 10, "y": 12}  # if we have multiple items with the same key
# the last value will be used
combined = {**first, **second, "z": 4}
print(combined)
