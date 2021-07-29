# to save information about a user
def save_user(**user):    #
    print(user)
    print(user["id"])  # TO ACCESS ANY INFORMATION OF THE USER
    print(user["name"])


save_user(id=1, name="Siddhant", age=18)


# output:
# {'id': 1, 'name': ' Siddhant', 'age': 18}
#
# THE OBJECT OUTPUT YOU SEE IS A DICTIONARY,
# IT IS ANOTHER COMPLEX TYPE OR DATA STRUCTURE IN PYTHON
