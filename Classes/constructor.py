from os import defpath


class Point:
    # self : is the reference of the current point object
    # to create a constructor
    def __init__(self, x, y):
        # above method to define a constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        


# here "point"  is object of class "Point"
point = Point(1, 2)
print(point.x)
print(point.y)
point.draw()
