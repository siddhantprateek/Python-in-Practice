# Tuple: is basically read-only list we use it contain a sequence of
# objects but we cannot modify the sequence we add or remove or modify
# an existing object


# we use parenthesis to define a Tuple
# even we can exclude parenthesis , python will assume it as a tuple


point1 = 1
print(type(point1))
# if we add comma to integer python treat it as a tuple
point2 = 3,
print(type(point2))

point = (1, 2)
print(type(point))
# to define empty tuple use empty parenthesis
# you can concatenate with another tuple
print(point + point2)
# repeat a tuple
point3 = (4, 5)*3
print(point3)

# you can convert a list or string or any iterable into tuple
name = tuple("Hi Siddhant")
number = tuple([1, 2])
print(name)
print(number)
# similar we can use to get object through its index or range of item
# cam unpack like list
print(name[1])
