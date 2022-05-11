# These are data types that are used to store values

a=10

# a the value given by the user
# 10 is the value

# Rules in naming variables
# 1.Special characters eg, $%#^ not allowed except "_"
_a=10 

#2.We need to start the name of the variable with an alphabet or _
# a-z|A-Z|_ -> The first char of the variable
 
aA=10
_aA=10
aA_=10

# 3. The next character after my first character can be anything
# (a-z|A-Z|_|0-9)

a123=10

# 4. Python supports multiple variable initialization
c=d=10
# Both c and d variables hold the same value

print(c)
print(d)

x,y=10,34

print(x)
print(y)

# 5. Lexical/ Grammer Rule ???
# ((letter|_) (letter|_|0-9))

# 6. Identifiers and Keywords
# Variables are alike to identifiers
# Keywords are variables specifically reserved by the programming langauge
# You cannot use a keyword as a name of a variable

# print,elsefif, switch, for, -35 keywords

_a=10

# If you are using "_" before any variable name this means you are declaring the variable as Private var
 
# The value of that variable cannot be overwritten
__a=10


r,s,t=1,2.09,"Kabarak"

print(type(r))
print(type(s))
print(type(t))

