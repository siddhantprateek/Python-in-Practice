for number in range(3):
    print("Hi", number + 1, (number + 1)*".")

# for <variable> in <range of items or strings>

# this changes as assign change in what for


for number in range(1, 10, 2):
    print("Hi", number, (number)*".")

name = "Siddhant"
# well to get characters and its index use enumerate function
#
for character in enumerate(name):
    print(character)

# to unpack the tuple
# so basically enumerate function group the character and its index
# into a tuple ,
# to unpack that tuple i passed two variable
# character and index
for character, index in enumerate(name):
    print(character, index)
