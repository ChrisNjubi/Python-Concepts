"""
 Python dictionaries are in the form of a key and value pair
1. Key- python immutable objects such numbers, strings, tuples
2. Val- Python objects

"""

# How are dictionaries created

D1 = {

    "Name":"Chris",
    "Age":23
}

print(type(D1))
print(D1)

D2 = {
    "Name": "Audi",
    "Model": "AudiA4 allroad",
    "Price": 45500,
    "Fit": "Luxury",
    "Speed": "True"
}

print("Name- {}".format(D2["Name"]))
print("Model- {}".format(D2["Model"]))
print("Price- {}".format(D2["Price"]))
print("Fit- {}".format(D2["Fit"]))
print("Speed- {}".format(D2["Speed"]))

"""
Updating key values in a dictionary
"""
# D2["Name"]=input("Enter name.......")
# D2["Model"]=input("Enter Model......")
# D2["Price"]=int(input("Enter price"))
# D2["Fit"]=input("Enter Fit........")
# D2["Speed"]=bool(input("Is it fast?"))
#
# print(D2)

# Deleting a value in python dictionary

D3 = {
    "Name":"C.Ronaldo",
    "Country": "Manu",
    "Club": "Manu",
    "Salary":26.52
}
print(D3)
del D3["Club"]

print(D3)


# Iterating through a dictionary

"""
Printing all key values
"""

for x in D3:
    print(x)


"""
Printing all values
"""

for x in D3:
    print(D3[x])

"""
Iterating through both key and values
"""

for key in D3:
    print(key, ":", D3[key])

"""
Dictionary that stores data in form a list 
"""

item={
    "Fruits": ["Mango","Banana", "Tree-Tomato"],
    "Price": 3000,
    "Size" : 10.4
}

print(item["Fruits"])

print(item["Fruits"][1])


# A dictionary within a dictionary
player = {
    "Name": "Messi",
    "Salary":{"Currency":"$", "Amount":23000,},
    "Clubs":{"France":"PSG","Spain":"Barcelona"},
    "Country":"Argentina"
}

print(player["Salary"])
print(player["Salary"]["Currency"])

print(player.get("Clubs").get("Spain"))
print(player.get("Salary").get("Amount"))

"""
Length of the dictionary
"""

print(len(player))

print(player.keys())


