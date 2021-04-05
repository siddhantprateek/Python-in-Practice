class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass

#             1             2
# greet of that class will be executed whose class argument is provided first


manager = Manager()
manager.greet()
