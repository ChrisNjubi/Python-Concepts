print(type("This is a string"))

# You can define a string using both double quotes and single quotes
a="Welcome home mom"
print(a)

b='Welcome Home Dad'
print(b)

# 
'''

Hey, my name is "Chris"

'''

print('Hey my name is "Chris"')

e= "Hey"

# 
g="""

Hey 
My name is Chris


"""
print(g)

# 
print("This is Chris's \"New\" house")

# Accessing values of a string
# All values are stored at a particular index
# The very first index starts from zero

name="Chris"

print(name[1])
# Slicing a String
print(name[0:4])

print(name[1:4:2])
print(name[::])
print(name[::2])
print(name[::1])
# Reversing a String
print(name[::-1])

# Length of the String
name="Walubengo"

print(len(name))

# Striping a String: Removing white Spaces

sentence="This is my ball  "

print(sentence.strip())

# converting string to lowercase and uppercase

print(sentence.upper())
print(sentence.lower())

# Splitting a String

abc="Hey, I'm in love"
# Splitting abc on the basis of coma
b= abc.split(",")
print(b[0])
print(b[1])

# Concatenation
# Both strings should be of the same data type
ab="Warrup"
cd="I'm Chris"

print(ab+cd)
print("10"+"10")

# Repeating the String
print("10"*4)
# Rule of bodmas
print("ba"+"na"*2)

# String Formatters
# f-strings
# format()
work="Safaricom"
print("I work at",work)

age=22.5
id=37145333

print(f"I work at {work} and I'm {age} year's old and my id is {id}")
print("I work at {} and I'm {} years old and my ID is {}".format(work,age,id))
print("I work at %s and I'm %f years old and my id is %d"%(work,age, id))