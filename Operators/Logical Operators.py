# And -> Returns true if both arguments are true 
# or -> Returns true if atleast one argument is true
# Not -> Returns the reverse


from operator import truediv


print(True and True)
print(1 and 0)

"""
a. if the value of x evaluates to true, then the result is the value y
b. if the value of x evaluates to false, then the result is the value x

"""
print(10 and 20)
print(0 and 20)

print(10 or 20)
print(0 or 20)

# username=input("Enter username:")
# password=input("Enter password:")

# if username=="Klamar" and password=="(0)(0)":
#     print("Valid User")
# else:
#     print("Invalid user")

print(not True)
print(not False)


a=10
print(not a==10)