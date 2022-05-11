"""
1. Tuple is used to store the sequence of IMMUTABLE objects
2. Mostly all the other operations are similar to a list
3. Created with the help of parenthesis ()
"""

stadiums= ("Old Trafford","Emirates","Etihad")
print(type(stadiums))

# We cannot re-assign values to a tuple after initialization
# stadiums[2]="Woodson Park"
print(stadiums)

"""
Tuple slicing/indexing

"""

num=(0,1,2,3,4,5,6)

print(num[0:])
print(num[:])
print(num[2:4])
print(num[-1:])
print(num[:-1])
print(num[:4])
print(num[::-1])

"""
Deleting an item from a tuple
"""
# You cannot delete an item from the tuple
# del num[2]
# print(num)


"""
Tuple Operations:

1. Repeatition
2. Concatenation
3. Membership operation
4. Iteration
"""

# repetition
name = ("Klamar","Chris")
print(name*2)

# Concatenation
name1=("Waluu",24)
print(name+name1)

# Membership operation
print("Klamar" in name)
print("Waluu" not in name1)

for i in ("Klamar","Chris"):
    print(i)


"""
Why do we use tuples instead lists in real programming?

Tuples are most preferred when we have values that are not supposed to change such as id, institution name
Lists stores mutable objects

"""


