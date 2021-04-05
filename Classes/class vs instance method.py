# The self is used to represent the instance of the class.
# With this keyword, you can access the attributes and methods of the class in python.
# It binds the attributes with the given arguments.
# ... In Python, we have methods that make the instance to be passed automatically,
# but not received automatically.


class Point:

    def __init__(self, x, y):
        self.x = x  # attributes
        self.y = y

    @classmethod  # decorator
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# point = Point(0, 0) also can be written with initial value (0,0) and wanted it
# repeat in several place in a programme (factory method)
point = Point.zero()
point.draw()
