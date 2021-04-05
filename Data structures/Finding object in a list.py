letters = ["a", "b", "c", "d", "e"]

# TO FIND THE INDEX OF AN OBJECT IN A LIST
print(letters.index("a"))

# TO FIND INDEX OF IN OBJECT THAT DOESN'T EXIST IN THE LIST
# YOU WILL GET A VALUE ERROR
# TO PREVENT THAT ERROR

if "f" in letters:
    print(letters.index("f"))
print("f DNE")

# ANOTHER WAY IS

# THIS WILL RETURN NUMBER OF OCCURRENCE OF LETTER IN LIST
print(letters.count("f"))
