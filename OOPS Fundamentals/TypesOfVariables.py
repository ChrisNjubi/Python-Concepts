"""
Two types of variables:
    Class variables/ static variables: Defined at the global level
    Instance Variables: Are always called from the instance of a class, ie, from the object of class

"""


class Person:
    # Static Variable
    legs = 2

    # Instance variables
    def __init__(self):
        self.name = "Chris"
        self.color = "Light Skin"


p1 = Person()
p2 = Person()

p2.name = "Brian"
p2.color = "Black"

Person.legs = 4

print(p1.name, p1.color, Person.legs)
print(p2.name, p2.color, Person.legs)
