class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub


class Mammal(Animal):  # it inherits all the features and all the methods of animal class
    def walk(self):
        print("walk")


class Fish(Animal):
    def walk(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
