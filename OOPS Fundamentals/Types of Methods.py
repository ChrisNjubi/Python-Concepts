"""
1. Instance Method -> Use to access instance variable of the class
2. Class Method -> Use to access static of the class
3. Static Method -> Standalone Method

"""


class Dog:
    legs = 4

    def __init__(self):
        self.name = "Chris"
        self.color = "Light Skin"

    # Instance Method becoz its beign called from the instance of the class(object D1)
    def getDogName(self):
        print(self.name)

    # Class method
    # The decorator below tells python that the below method is a class method
    @classmethod
    def getDogLegs(cls):
        print(cls.legs)

    # Remove self or cls from the method parameter to make the function static, ie, it can be accessed anywhere
    # with any object
    # Static Method
    @staticmethod
    def generalInformation():
        print("Beware of Dogs")


D1 = Dog()

# Accessing instance method
D1.getDogName()

# Accessing class method
D1.getDogLegs()

# You can call the class method directly with the class name
Dog.getDogLegs()

# Access static method
Dog.generalInformation()

