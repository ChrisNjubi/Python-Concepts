"""
1. Block of code used to perform a specific action
2. Reusable block
3. Can have parameters
4. Collection of multiple functions creates a program
5. Pre-defined functions print() and sort() etc

 Syntax:
    def function_name():
        statement/code to be executed

    1.Def is a keyword
    2.Function name should start with small letter
    3.If your function name has multiple or more words separate them using underscore

"""


def print_my_name():
    print("My name is Chris")


print_my_name()


# Passing a parameter within a function


def print_my_name_as(Name):
    print("My name is:" + Name)


print_my_name_as("Klamar")


# Defining return types to a function
# A function can return a string type, boolean value, numeric value


def print_my_school(school):
    return "My School is: " + school


# The function is returning a string value and storing it in variable school and then printing it
school = print_my_school("Kabarak")
print(school)


# Providing multiple parameters to a function
def get_user_details(name, age, salary):
    # print("Name is: ",name, "Salary is:",salary, "Age is: ",age)
    print("Name is: " + name + "Salary is: " + str(salary) + "Age is: " + str(age))


#     You can use any of the above


get_user_details("Mike", 35000, 32)

# changing sequence of the arguments
get_user_details(name="Moses", age=45, salary=4000)

"""
Parameters are given when defining the function and arguments are given when calling the function

"""

"""
Types of arguments:
    
    1. Required arguments
    2. Keyword arguments
    3. Default arguments
    4. Variable length arguments
    
"""


# Required arguments

def req_arguments(a, b):
    print(a + b)


req_arguments(20, 46)  # required arguments


# Keyword arguments
def cars(name, type, price):
    print("Name is: ", name, "Type is: ", type, "Price is: ", price)


cars(name="Audi", type="AudiA6", price=5000000)  # Keyword arguments


# Default arguments
def default_arguments(player, team="Manu"):
    print("Player - {}".format(player))
    print("Team - {}".format(team))


default_arguments("CR7")
default_arguments("Bruno", "CHelsea")


# Variable length arguments
# We have scenarios where total number of arguments or parameters are not fixed

def var_argument(school, *name):
    # School is constant
    print(school)
    for i in name:
        print(i)


# By default, name will be accepted in form of a tuple

var_argument("Kabianga","Mercy", "Njoki", "Rahab", "eKYC", "Laban", 12, 45.5, True)
