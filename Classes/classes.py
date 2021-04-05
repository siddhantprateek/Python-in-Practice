#  Class is a blueprint for creating new objects
#  object : instance of a class

# e.x.
#  # Class: Humans
#  # objects: John ,Mary , Jack


# __init__()
# All classes have a function called __init__(),
# which is always executed when the class is being initiated.

# "__init__" is a reserved method in python classes. ... This method is called when an
# object is created from a class and it allows the class to initialize the attributes of the class.

# Use the __init__() function to assign values to object properties,
#  or other operations that are necessary to do when the object is being created:

# NOTE:  The __init__() function is called automatically
#        every time the class is being used to create a new object.

# A class is a block of code that holds various functions. Because they
# are located inside a class they are named methods but mean the same
# thing.

# In addition variables that are stored inside a class are named attributes.

# The point of a class is to call the class later allowing you
# to access as many functions or (methods) as you would like with the same
# class name.

# These methods are grouped together under one class name due
# to them working in association with eachother in some way.


class Person:

    def __init__(self, name, age):  # the Constructor
        self.name = name
        self.age = age


p1 = Person('Siddhant', 19)

print(f"Name : {p1.name}")
print(f"age : {p1.age}")
