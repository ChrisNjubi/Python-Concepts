"""
Repeatition Operation
"""

b=["Chris","Audi",22,"Safaricom","Quality Assurance",3+4j]

print(b*2)

"""
Concatenation

"""

c=["Waluu","Benz",24,"Quality Assurance",True]

print(b+c)

"""
Membership Operations

"""

print("Waluu" in c)
print("Audi" not in b)

"""
Iteration Operation

"""

for x in b:
    print(x)

"""
Length Operation

"""

print(len(b))

"""
Getting the minimum value and maximum value in a string
"""

marks=[422,368,255,231,190]
print(max(marks))
print(min(marks))

"""
Convert a string to a list
"""

string="Waluu"
print(list(string))