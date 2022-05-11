# Break statements are used to break the current loop and resume the other code
for i in range(10):
    if i == 7:
        print("Executing break at", i)
        break
    print("Printing the value as", i)
print("Outside the loop")

# Continue statements are used to skip the current iteration and continue with the next iteration
"""
for example let's use 3
3 does not satisfy the if condition hence the "even" statement will be skipped and the next statement executed

"""
print("---------printing odd numbers------")
for i in range(10):
    if i%2==0:
        print("Even number is:",i)
        continue
    print("Odd number is:",i)

print("---------------")
for i in range(10):
    if i == 7:
        print(i)
        break
    elif i == 5:
        continue
    print(i)