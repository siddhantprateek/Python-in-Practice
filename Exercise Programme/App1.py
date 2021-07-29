# Converting Weight programme
# since input is in string so we have to
weight_pounds = input(" Enter your weight in(lb): ")
# ERROR : weight_kg = (weight_pounds) * 0.45                    # we have to convert string into float
# print(weight_kg)

# Output:

# Enter your weight in(lb): 175
# Traceback (most recent call last):

#    weight_kg = weight_pounds * 0.45
# TypeError: can't multiply sequence by non-int of type 'float'

# Process finished with exit code 1
weight_kg: float = int(weight_pounds) * 0.45
print(weight_kg)
# print(weight_kg)
