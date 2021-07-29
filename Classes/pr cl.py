class Person:

    def __init__(user, name, age):
        user.name = name
        user.age = age


p1 = Person('Siddhant', 19)

print(f"Name : {p1.name}")
print(f"age : {p1.age}")
