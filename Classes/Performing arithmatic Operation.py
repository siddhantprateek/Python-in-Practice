class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # to add two objects we have a magic method __add__

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 20)
other = Point(1, 2)
combine = point + other
print(point + other)
print(combine.x)
