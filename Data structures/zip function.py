
# IN THIS ZIP FXN WE COMBINE EACH OBJECT FROM THEIR POSITION
# [(1, 10), (2, 20), (3, 30)]
# Suppose that we already had a list of names and a list of heights:

# names = ['Jenny', 'Alex', 'Sam', 'Grace']
# heights = [61, 70, 67, 65]
# If we wanted to create a list of lists that paired each name with a height,
# we could use the command zip. zip takes two (or more) lists as inputs and
# returns an object that contains a list of pairs.
# Each pair contains one element from each of the inputs.
# You won’t be able to see much about this object from just printing it:

# names_and_heights = zip(names, heights)
# print(names_and_heights)

# because it will return the location of this object in memory.
# Output would look something like this:

# <zip object at 0x7f1631e86b48>


# To see the nested lists, you can convert the zip object to a list first:

list1 = [1, 2, 3]
list2 = [10, 20, 30]

f_list = zip(list1, list2)
print(f_list)
print(f"Memory address of Final list : {f_list}")
print(f"Final list : {list(f_list)}")


# zip takes two (or more) lists as inputs and returns an object that contains a list of pairs.

print(list(zip(list1, list2)))

# or we can pass a string
print(list(zip("abc", list1, list2)))
