# value = []
# # loop variable is x

# for x in range(5):
#     value.append(x*2)
# # in each iteration we get a value of 'x' multiplied by 2 and added to the empty list


# the line of code is exactly equal to above lines
# we can convert into set by replacinf [] ---- {}


# for list comprehension
# [] for defining a list and comprehension expression which is here is (x*2)

# [expression for item in items]
# to covert it into a set instead if [] -> {}


values = {x*2 for x in range(5)}
print(values)

# sets and dictionary are represented as same be but in dictionary
# we have key for a value whereas in set we have only values

# key is (x:)

num = {x: x*2 for x in range(5)}  # Dictionary comprehension
print(num)
