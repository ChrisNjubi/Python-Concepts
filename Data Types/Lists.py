"""
    1. List is a consecutive collection of related items/words
    2. Represents a group of values as a single entity, order is very important
    3. It allows duplicate values as well
    4. Values are seperated by commas
    5. It is represented by a square bracket []
"""

a=[] #empty list
b= [1,2,3,"Chris",3+2j,True]
print(type(b))

"""
2. Order is preserved
"""

print(b[4])

"""
3. Lists allow duplicate values
"""

c=[4,5,5,"Walue",4]


"""
4. Lists are mutable
"""

t=["Manu","Liver","Mancity"]
print(t)

t.append("Chelsea")
print(t)

# Fetch values from multiple indexes of the list
Safaricom = ["Waluu","Quality Assurance", 2384]

print(f"Name is {Safaricom[0]}, department is {Safaricom[1]} and Id is {Safaricom[2]}")

# List Slicing

c = [0,1,2,3,4,5,6]

print(c[1:]) #0,1,2,3,4,5,6
print(c[:])  #0,1,2,3,4,5,6
print(c[2:4]) #2,3
print(c[:4]) #0,1,2,3
print(c[-1:]) #6
print(c[:-1]) #0,1,2,3,4,5
print(c[::-1])#6,5,4,3,2,1,0
"""
Updating values in a list

"""

d=[2,4.5,3.4,5,6,7,4,6,9,10]

print(d)

d[3] = 4

print(d)

d[1:4]=["Manu","Mancity","Liverpool"]
print(d)


"""
Deleting values in a list

"""

e=["Njoki","Chep","Tess","Maureen","Eliza"]
print(e)
del e[4]
print(e)

"""
Sorting a list

"""
# You can
f=[1,3,6,5,2,4,7]
print(f)
f.sort()
print(f)

f.sort(reverse=True)
print(f)






