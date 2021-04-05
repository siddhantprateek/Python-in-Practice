# Dealing we large sequence of numbers we use Array it take less space
# to use array we need to import it from array module

from array import array

# here (i) means integer

numbers = array("i", [1, 2, 3])

# array("<Typecode>",<List of objects> )
numbers.append(4)
# insert(<Index>, <object to be inserted>) to add at specific index
# Every object in this are integer type and can be replaced by an
# integer only, not other type

numbers.insert(2, 5)  # insert(<index> , <Item to insert>)
print(numbers)
