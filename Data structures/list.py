# A list is an ordered set of objects in Python.

# Notice that:

# A list begins and ends with square brackets ([ and ]).
# Each item (i.e., 67 or 70) is separated by a comma (,)
# It’s considered good practice to insert a space () after each comma, but your code will run just fine if you forget the space.

# List of Lists
# We’ve seen that the items in a list can be numbers or strings.
# They can also be other lists!


letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0]*5  # YOU DON'T HAVE TO WRITE MULTIPLE 0
combine = letters + zeros
combine_2 = letters + matrix
print(combine_2)
print(matrix)
print(combine)


numbers = list(range(20))
print(numbers)
characters = list("Siddhant Prateek")

print(len(characters))  # TOTAL NO. OF CHARACTERS IN LIST
print(characters)
print(len(numbers))
