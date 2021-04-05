# Scope : refers to the the region of the function where the variable is defined
# there two types of variable local variable , global variable

message = "a"  # global variable


def greet(name):
    message = "b"  # message is the variable and the scope of thi variable is greet fxn ,it only exist inside of this fxn
    # name and message variable are called the local variables , does not exist anywhere else

# print(message)


greet("Siddhant")
print(message)
