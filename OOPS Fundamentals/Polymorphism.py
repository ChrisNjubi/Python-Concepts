"""

Polymorphism describes situations where something occurs in several forms

1. Operator Overloading
2. Method Overloading / Overriding
3. Constructor Overloading/ Overriding

"""
# overloading the + operator
x = 3
y = 4
t = "Hey"; u = "How are you"
print(x + y) # Using the operator tot perform arithmetic operation
print(t +  " " + u + str(x)) # Using the operator to concatenate strings
"""


1. Operand Overloading 
<operand><operator><operand>
1+2=-1


"""


class OperatorOverloading:
    def __init__(self, pages):
        # Create a global pages variable and assign it to local variable value
        self.pages = pages

    #     Call a pre-defined function: Addition pre-defined function
    def __add__(self, other):
        #         Change function functionality
        totalPages = self.pages - other.pages
        return totalPages


obj1 = OperatorOverloading(5)
obj2 = OperatorOverloading(10)

print(obj1 + obj2)

"""
2. Method Overloading : Same method with different parameters
First lets define difference between a method and a function in python:

A method is a function defined inside a class
A function is a block of code that performs a specific task
"""
# class MethodOverloading:
#
#
#     def add(self, a, b):
#         return a + b
#
#     def add(self, a, b, c):
#         return a + b + c
#
#
# obj3 = MethodOverloading()
# print(obj3.add(10, 34))
# print(obj3.add(10, 20, 30))

"""
Method overloading is not supported in python
Constructor overloading is not supported in python

"""

# class ConstructorOverloading:
#
#     def __init__(self):
#         print("Inside default constructor")
#
#     def __init__(self, name):
#         self.name=name
#         print("Inside parameterized constructor")
#
# obj4=ConstructorOverloading
#
# print(obj4.__init__("chris"))


"""
3. Method Overriding and Constructor Overriding

In python, the constructor is always executed first
Method/ constructor overriding necessarily does not mean replacing existing code rather modifying the existing code.
"""


class MethodOverridingBase:
    def a(self):
        print("Inside base class")

    def __init__(self):
        print("Base Class")


class MethodOverridingDerived(MethodOverridingBase):
    # Calling functionality of parent class alongside the parent class
    def a(self):
        super().a()
        print("Inside Derived class")

    def __init__(self):
        super().__init__()
        print("Child class")


obj6 = MethodOverridingDerived()
obj6.a()

"""

4 Function overloading
let's use an inbuilt len() function

"""
print(len("Hello"))
print(len([2, 5, 8, 10, 11, 21, 43]))
print(len({"Kenya":"Nairobi", "Uganda":"Kampala"}))
print(len((2, 3, 6, 9, 10)))