# Dictionaries(Data Structure): That is collection of key menu pairs
# example : Phone book (name ->contact)

point = {"x": 1, "y": 2}
# dict() fxn can be used for to create a dictionary
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 10

#   (name ->contact)  We can understand through this fxn that a string provinding an
# integer
# As we see in Phone Diary with Name and contact details
print(point["x"])

point["z"] = 20

if "a" in point:
    print(point["a"])
print(point.get("a"))
del point["x"]
print(point)

# How to loop over dictionary
# Our loop variable will hold key on an item
#

for key in point:
    print(key, point[key])
# will give the key and the number holding it

# another way to iterate over a dictionary
for x in point.items():
    print(x)
# we can unpack the tuples

for key, value in point.items():
    print(key, value)
