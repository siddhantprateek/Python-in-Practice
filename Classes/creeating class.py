class Point:
    # inside this block we define all the Fxn related to point

    # all fxn in classes must have at least one parameter.

    def draw(self):
        print("Draw")


# to create a "point" object we call this class as a function
point = Point()  # returns a  point object

print(type(point))

# to "point" belong to "Point" class, there is fxn called isinstance
# to determine the instance of the object

print(isinstance(point, Point))  # isinstance( <object>, <Class>)
print(isinstance(point, int))
