"""
1. Similar to list
2. It can store different types of values (Objects) String, Int, float, Bool etc
3. Set can have duplicate values
4. It's a collection which is unordered and unindexed : Run the print(Set) a couple of times for illustration
5. Sets have no supported operands such repetition, concatenation unlike the list

"""

S1={"Selenium",46,45, 34, True, "Appium"}

print(type(S1))
print(S1)
print(len(S1))

# print all elements using a loop
for i in S1:
    print(i)

# It cannot have duplicate values
S2={"Radio", "Television",34,56,34}

print(len(S2))
print(S2)


# Add more items to the set
S2.add("Bluetooth")
print(S2)

# Deleting an item from the set
S1.remove(True)
print(S1)
S2.discard(34)
print(S2)

"""
Difference between discard and remove:
    When you want to remove an item from a set which is initially not there, and use remove it will throw an
    exception/error while using discard no error will be reported.
"""

# Copying values of one set to another set
S3=S2.copy()
print("-----------")

print(S3)

