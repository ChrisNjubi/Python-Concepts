

# write a program using if conditions to print "Odd" if the number is odd,
# "First even" if the number is even and in the range of 2 - 10,
# "Second even" if the number is even and in the range of 12 - 30,
#  "Last even" if the number is even and greater than 30,
# and "Out of range" if the number is less than 1.
# note: You can combine ifs, elifs and else


# number=int(input("Enter a number:"))
#
# if number % 2 != 0:
#     if number > 0:
#         print("Odd")
# if number % 2 != 0:
#     if number < 1:
#         print("Out of range")
# if number % 2 == 0:
#     if number in range(2,11):
#         print("First even")
# if number % 2 == 0:
#     if number in range(12,31):
#         print("Second Even")
# if number % 2 == 0:
#     if number>30:
#         print("Last even")
# if number%2 == 0:
#     if number < 1:
#         print("Out of range")


"""
Use an if statement together with multiple elifs to display. "One" if the entered number is 1,
"Two" if the entered number is 2,
"Three" if the entered number is 3,
"Four" if the entered number is 4
and "Five" if the entered number is 5
Note: the program should accept the input from the user.Also print "Unknown" if entered number is greater than 5
and "Unknown" if entered number if less than 1

"""
# a=int(input("Enter a number:"))
#
# if a < 1:
#     print("Unknown")
# elif a == 1:
#     print("One")
# elif a == 2:
#     print("Two")
# elif a == 3:
#     print("Three")
# elif a == 4:
#     print("four")
# elif a == 5:
#     print("Five")
# else:
#     print("Unknown")


# use for loop to iterate a list of 10 numbers (ie. from 1 - 10),
# if the a number in the list equals 5, skip it and
# if the number equals 9, terminate the iteration

#
# for i in range(10):
#     if i==9:
#         print(i)
#         break
#     elif i==5:
#         continue
#     print(i)

# Write a program to does the following on a given array
# on one line display the elements of the array,
# on another line display sum of the elements
# and on another line also display the elements in reversed order
# """

A=[1,2,3,4,5,6]
for x in A:
    print(x, end= " ")

sum=0
for i in range(len(A)):
    sum=sum+A[i]
print("\n", sum)


for i in reversed(A):
    print(i, end = " ")



