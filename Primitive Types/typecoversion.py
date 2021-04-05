x = input("x: ")
print(type(x))

# y = x + 1  THE PROBLEM IN THIS CODE WAS 'X' WAS A STRING, SO WE CANNOT ADD STRING TO A NUMBER,SO
# WE HAVE TO CONVERT X TO AN INTEGER

y = int(x) + 1
print(f"x: {x} , y: {y} ")
