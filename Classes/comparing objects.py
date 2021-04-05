class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(1, 2)
other = Point(1, 2)

print(point == other)
# we get false because the equality operator compares the the addresses of the
# objects which are not same.
# before we define __eq__ magic method

# to solve we need magic methods
point = Point(10, 20)
other = Point(1, 2)

# greater then operator is supported with the the instances of the class
# for this we require another magic method called __gt__
print(point > other)
print(point < other)
