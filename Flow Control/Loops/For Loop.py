
"""
# Loops are iterative statements: When you want to execute a particular statement multiple times
# 1. For loop
# 2. While loop
# Python has no do while loop
# For loop

For every x (x can be a variable that holds a value) in the sequence to perform some activity, which means
every element which is available in the sequence, range, tuple, list or dictionary

Syntax:

for x in sequence:
    statements


for 1st Iteration

x=0
for 0 in [0,1,2,3,4,5,6,7,8,9,]: True
    print("Chris")
x+1

for 2nd Iteration
.............

"""


sequence="Chris"
# Initialize the index: start at zero
# Initialization means giving an initial value
i=0
# x is the elements
for x in sequence:
    #  print("The character present at {}, index - {}".format(i,x))
    print("The character present at {1}, index - {0}".format(i,x))
    i=i+1

for x in range(10): # 0-(n-1): 0-9
    print("Chris")

for x in range (1,11):
    print("Chris",x)

for x in range(2,30,3):
    print(x)

n=int(input("Enter the number:"))
for x in range(1,11):
    # n is the number we're going to input
    print(n,"*",x,"=",n*x)


# Eval is a function that takes in numerical values in any format either list, tuple
List = eval(input("Enter the numbers for addition:"))
sum=0

for x in List:
    sum=sum+x
print("The sum is:", sum)


string= "My name is Chris"
s=string.split()

for x in s:
    print(x)