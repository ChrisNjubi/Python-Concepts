"""
Inheritance:

    Class A ---> Base Class / Parent Class
        def add (self):

    Class B -----> Derived Class/ Child class

So from inheritance we can access members, properties and methods from another class (Parent Class)

"""

"""
1. Single- level Inheritance
"""


class Animal():
    name = "Chris"

    def a(self):
        print("I am inside Animal")


class Mammal(Animal):
    def b(self):
        print("I am inside Mammal")


Mamm = Mammal()
Mamm.b()
"""
# I should be able to call function inside Animal class with reference of "Mamm" of b class
# since Mammal Class has inherited all properties defined in Animal Class
"""
Mamm.a()
# The child class can inherit any type properties from the parent class
print(Mamm.name)

"""
2. Multilevel inheritance:
    A class can be derived from one class, which is already derived from another class
"""


class Car():
    def car(self):
        print("This is a Car")


class Mercedes(Car):
    def brand(self):
        print("I am inside an Audi")


class AudiA6(Mercedes):
    def type(self):
        print("I am inside an Audi A6")


Gari = AudiA6()
Gari.car()
Gari.brand()
Gari.type()

"""
Multiple Inheritance:
    A class can inherit features from more than one parent class
"""


class England():
    def country(self):
        print("This is English Football")


class EPL():
    def title(self):
        print("This is the English Premier league")


class Manu(EPL, England):
    def team(self):
        print("This is Manchester")


KLabu = Manu()
KLabu.country()
KLabu.title()
KLabu.team()

"""
Method Resolution Order:
    Defines the order in which the base classes are searched when executing the method. Based on heirarchy defined
    during class inheritance
"""


class England():
    def country(self):
        print("This is English Football")

    def motto(self):
        print("The Home of Champions")


class EPL():
    def title(self):
        print("This is the English Premier league")

    # Python allows same function in different classes
    def motto(self):
        print("The Home of Champions")


class Manu(EPL, England):
    def team(self):
        print("This is Manchester")

Roro=Manu()
Roro.motto() # Will be called from EPL class since it is the first class we inherited in the hierarchy
