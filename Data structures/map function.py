# map function in pythonPython By Bright Butterfly on May 11 2020
# Python program to demonstrate working
# of map.

# Return double of n
# def addition(n):
#     return n + n


# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(lambda n: n + n, numbers)
# map function provides the address to the result
print(result)
print(list(result))


# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))
