def x(a): return a + 10
# lambda a: a * n


print(x(5))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

# execution goes like
# mydoubler = lambda a: a*2
# which converts into
# def mydoubler(a): return a*2

print(mydoubler(11))
