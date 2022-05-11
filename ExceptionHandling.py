"""
Exceptions/ Errors

Runtime error -> Error we get after running code
Compile time error -> Incorrect syntax

Exceptions are disruptions to the flow of the program
If we code anything that is not logical flow of our program will be disrupted and eventually throw an exception

"""

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
#
# c = a / b
#
# print("Result is {}".format(c))

"""
The above code might throw an exception if you input non-logical arguments, for example, 20/0
How do you handle exceptions

try:
    {---------------}
except:
    {----------------}
    

In the try section we will write our initial code and in case it throws an exception code in the except section will be executed

We can also add

else:

This code in this block is only executed only if there is no exception. For example you are writing to a file and you
want to close the file if no exception is captured. The best place to write your close file code is in the else block
"""

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    c = a / b

    print("Result is {}".format(c))
except (ZeroDivisionError, ValueError,IndentationError):
    print("Please input a valid number")

else:
    print("Inside an Else block")

#     This block is executed whether there is an exception or not
finally:
    print("I am always executed")


print("This is outside except block")


"""
BASE EXCEPTION
    1. Exception
        a. Attribute Exception/ Error -> If we try to access any function that is not there in the class
        b. Arithmetic Exception/ Error
            1. ZeroDivisionError
            2. FloatingPointError
            3. Overflow Error -> whenever we have overflow of memory
        c. EOF Exception (End of File) -> Trying to compare two files
        d. Name exception
    2. System Exit Exception -> An exception is captured relating to the Operating System
    3. Generator Exit -> 
    4. Keyboard Interrupt 

"""