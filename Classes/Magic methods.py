# The "self" is used to represent the instance of the class.
# With this keyword, you can access the attributes and methods of the class in python.
# It binds the attributes with the given arguments.
# ... In Python, we have methods that make the instance to be passed automatically,
# but not received automatically.


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)


print(str(point))
