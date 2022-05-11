"""
It is conditional operator
There is no specific keyword for ternary operator 
var= first value if condition ELse second value

"""

a=30
b=45
c=60 if a<b else 76
print(c)

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
max=a if a>b else b
print(max)