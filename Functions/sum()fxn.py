"""
sum(iterable, start)
iterable : iterable can be anything list , tuples or dictionaries ,
 but most importantly it should be numbers.
start : this start is added to the sum of
numbers in the iterable.
If start is not given in the syntax , it is assumed to be 0.
"""
"""
sum(a)
a is the list , it adds up all the numbers in the
list a and takes start to be 0, so returning
only the sum of the numbers in the list.

sum(a, start)
this returns the sum of the list + start

"""
numbers = [1, 2, 3, 4, 5, 1, 4, 5]
# start parameter is not provided
Sum = sum(numbers)
print(Sum)
# start = 10
Sum = sum(numbers, 10)
print(Sum)


############################################
numbers = [1, 2, 3, 4, 5, 1, 4, 5]
# start = 10
Sum = sum(numbers)
average = Sum/len(numbers)
print(average)
############################################
