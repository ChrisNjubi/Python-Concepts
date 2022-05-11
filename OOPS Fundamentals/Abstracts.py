"""
We are importing ABC abstract class and abstractmethod from abc module

"""

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def breathe(self):
        pass

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def die(self):
        pass


"""
Since we are inheriting Animal abstract class, Dog and Lion class MUST implement all the abstract methods of the 
class Animal 
If failure to implement the abstract methods, it will result to failure in instantiating our child classes
Basically, we force child classes of the base abstract class to inherit all abstract methods of the abstract class.
AN abstract class may have both abstract methods and normal methods.
"""


class Dog(Animal):
    def move(self):
        print("Dog moves")

    def breathe(self):
        print("Dog breathes")

    def feed(self):
        print("Dog eats")

    def die(self):
        print("Dog dies")


class Lion(Animal):
    def move(self):
        print("Lion moves")

    def breathe(self):
        print("Lion breathes")

    def feed(self):
        print("Lion eats")

    def die(self):
        print("Lion dies")


mnyama = Dog()
mnyama.move()

mnyama1 = Lion()
mnyama1.move()



"""
Instantiating is creating an object of a class
AN abstract class is a class that contains one or more abstract methods
AN abstract method is a method that has no implementation
We cannot instantiate an abstract class
"""
