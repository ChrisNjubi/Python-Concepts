"""
1. Referred to as the first function of the class
2. All classes have this function which is always executed when the class is being initiated or an object of the
    class is created.

"""


class practice:

    def __init__(self):
        print("Inside constructor")

    def add(self):
        print("Addding something")


# Constructor is called automatically. You need not to call them explicitly using the reference
a = practice()

a.add()


# Constructors can also be parameterized
# Constructor overloading is not allowed in python, ie, no multiple parameterized constructors

class emp:
    def __init__(self, name, id):
        # declare some global variables and assign them to the local variables (parameters)
        self.name = name
        self.id = id

    def display(self):
        print("Name is: ", self.name)
        print("Id is: ", self.id)


# create an object of the above class

f = emp("Richard", 76)
# Call the function
f.display()

g = emp("chris", 45)
g.display()

