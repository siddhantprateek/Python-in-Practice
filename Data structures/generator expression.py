# creating a list with list comprehension expression
# then we iterate over all the number over the list


# values = [x*2 for x in range(10)]
# for x in values:
#     print(x)


# perhaps in some cases you would working on large number
# of data , you would not lke to store that data in your memory

# it is more efficient to use generator objects
# generator objects are iterable
# in each iteration they give out the value

from sys import getsizeof

values = (x*2 for x in range(10000))
# values is no longer a list it is a generator object
# in bytes and does not change iys size
print("generator:", getsizeof(values), "b")
# print(values)
# for x in values:
#     print(x)
values = [x*2 for x in range(10000)]
print("list:", getsizeof(values), "b")

# how to get the size of an object
