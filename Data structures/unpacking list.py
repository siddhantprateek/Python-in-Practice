numbers = [1, 2, 3, 4, 5, 6]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# (or)

# IF WE MISS TO ASSIGN ONE OF THE VARIABLE THERE WILL BE AN ERROR SAYING : ValueError: too many values to unpack (expected 2)
#
#first, second, third = numbers

# TO SOLVE THIS ISSUE WE CAN ASSIGN REST IN OTHER SET OF LIST


# when assign a parameter with asterisk python will pack all the argument into a list
first, second, *others = numbers
print(second)
print(others)
