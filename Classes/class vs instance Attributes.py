# Attributes : a piece of information which determines the
#               properties of a field or tag in a database
#               or a string of characters in a display.

# The self is used to represent the instance of the class.
# With this keyword, you can access the attributes and methods of the class in python.
# It binds the attributes with the given arguments.
# ... In Python, we have methods that make the instance to be passed automatically,
# but not received automatically.

# __init__(self, [...)
# The initializer for the class.
# It gets passed whatever the primary constructor was called with
# (so, for example, if we called x = SomeClass(10, 'foo'),
# __init__ would get passed 10 and 'foo' as arguments.
# __init__ is almost universally used in Python class definitions.


class Point:
    default_color = "red"  # class level attributes

    def __init__(self, x, y):
        self.x = x  # attributes
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# class attributes a shared across all across the instances of a class
point = Point(1, 2)
print(point.default_color)
point.z = 10
point.draw()
# we define a object outside the class because object in python dynamic similar to java script
# In python we don't have to define all the attributes in a constructor
# we can define it  later,  whenever we need .

# all the attributes we have defined x, y, and z are called instance attributes
# or these are attributes belong to point instances or point objects

# every point object can have different value for these attributes

# Ex.
Point.default_color = "Yellow"
another = Point(3, 4)
print(another.default_color)
another.draw()

# another point object can be created for different set of values
