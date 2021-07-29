class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walks(self):
        return True

    def bark(self):
        return "woof!"
# INHERIT FROM PARENT CLASS DOG
# ALL BELOW ARE CHILD CLASS


class Samoyed(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness) # to call function from parent class or inherit we call a super() function
    #


    # Polymorphism
    # let the sub class follow different set of rules
    # Polymorphism: it is ability of a object to behave in multiple forms.
    def bark(self):
        return "Arf! arf!"


class Poodle(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness) 

    def shedding_amount(self):
        return 0


class GoldenRetriever(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def fetch_ability(self):
        if self.age < 2:
            return 8
        elif self.age < 10:
            return 10
        else:
            return 7


# MULTIPLE INHERITANCE
class GoldenDoodle(Poodle, GoldenRetriever):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    # Polymorphism
    # Polymorphism: it is ability of a object to behave in multiple forms.
    def bark(self):
        return "ARoo!"


sammy = Samoyed("sammy", 2, 10)
print(sammy.name, sammy.age, sammy.friendliness)
print(sammy.likes_walks())
# sammy.fetch_ability()
generic_doggo = Dog('Gene', 10, 10)
goldie = GoldenDoodle("Goldie", 1, 10)
print(goldie.name, goldie.age, goldie.friendliness)
print(goldie.likes_walks())
print(goldie.shedding_amount())
print(goldie.fetch_ability())

print(sammy.bark())
print(goldie.bark())
print(generic_doggo.bark())
