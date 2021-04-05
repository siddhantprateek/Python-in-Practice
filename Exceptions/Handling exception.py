# exception is an kind of an error that terminates the execution of programmme

##################
# try:
#     age = int(input("age:"))

# except ValueError:
#     print("You didn't enter valid age ")


# else:
#     print("No exception were thrown")

# print("execution continues")
########################


# we can optional define a variable that will include the detail aboutthe exception

try:
    age = int(input("age:"))

except ValueError as ex:
    print("You didn't enter valid age ")
    print(ex)
    print(type(ex))

else:
    print("No exception were thrown")

print("execution continues")
