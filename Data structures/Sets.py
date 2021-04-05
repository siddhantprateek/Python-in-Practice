# Sets: it is data structure
# it is collections with no duplicates

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
# we use curly braces to define set
second = {1, 5}
# second.add(5)
# second.remove(5)
# len(second)

# we can get a union of two sets
print(first | second)
print(first & second)  # gets common item in both the sets
print(first)
print(first - second)  # to get difference of two sets
print(first ^ second)  # no common value

# set are un order collection we get item by passing an index
# #items are not in sequence ,we can't access them using an index

# can check item in the set
if 1 in first:
    print("yes")
