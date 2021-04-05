name = input('What is your name? ')
print('Hi ' + name)
color = input('What is your favorite color? ')
print(name + ' likes ' + color)

# Converting String into integer

birth_year = input(' Birth Year: ')
# define the class the birth_year belong
print(type(birth_year))
# this how it converts a string into an integer
age = 2020 - int(birth_year)


# If string is not converted into the
# programme will show Type Error where Integer is subtracted by
# by String.

print(type(age))                        # define the class the age belong
print(age)
