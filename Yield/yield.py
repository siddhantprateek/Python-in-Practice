def counter():
    x = 0
    while x < 5:
        yield x
        # incrementing the value of x
        x += 1