letters = ["a", "b", "c"]

# TO GET INDEX OF EACH ITEM THERE IS A BUILT IN FXN CALLED ENUMERATE()
# WHICH WILL RETURN ENUMERATE OBJECT WHICH IS ITERABLE
# IN EACH ITERATION THE ENUMERATE OBJECT WILL GIVE US A TUPLE
for letter in enumerate(letters):
    print(letter)

# for letter in enumerate(letters):
#     print(letter[0], letter[1])
# SYNTAX ABOVE IS UGLY
# OR()
# INSTEAD OF UNPACKING EARLIER
# item(0,"a")
# index, letter = item
# WE CAN UNPACK ON FOR LOOP ITSELF
for index, letter in enumerate(letters):
    print(index, letter)

for letter in letters:
    print(letter)
