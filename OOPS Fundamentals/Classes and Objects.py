"""
OOPS concepts / Procedural Langauge (Step by step implementation of the code)

What is a class?

1. A class can be defined as a blueprint / template which describes the state/ behaviour of its object
2 . Class is a logical entity: What we access is the properties. We cannot see the blueprint
3. A class is used to create different objects
4. A class can contain variable, constructors
5. Class is a combination of data members and data functions


Syntax:
    class <classname>:
        statements
"""

# Class creation
class Human:
    eyes = "Blue"
    nose = "Big"

    # self is a keyword through which we can access the attributes and methods of a class in python
    # self represents the instance of that class
    def eyes_function(self, color):
        print("This is an organ to see: " +color)

    def ears_function(self, size):
        print("This is an organ to hear - {}".format(size))

    def nose_function(self, shape):
        print("This is an organ to smell: ", shape)


"""
An object is an instance of a class.
Therefore a class can have multiple unique objects
Instead of re-writing code you can create multiple objects calling unique functionalities of the class and
re-executing th code again and again
"""


# Creating an object of a class
"""
Inorder to access the functions inside the class, you need to first create the object and call the functions as
below
To access methods from a class:

"""
a = Human()

a.nose_function("Circle")
a.ears_function("Large")
a.eyes_function("Blue")


b= Human()

b.eyes_function("White")
b.ears_function("Small")
b.nose_function("Triangle")

