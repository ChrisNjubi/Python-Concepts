# If the condition specified is true, python will execute the if statement otherwise if false python will
# skip the if statement

a=46
b=22

if a>b:
    print("A is greater than B")
else:
    print("B is greater than A")


# What is we want to test multiple conditions, we use else if

marks=int(input("Enter marks: "))
section=input("Enter the section:")

if marks == 100:
    # Nested if: IF block within an If block
    if section=="A":
        print("Brilliant class")
    grade="A"
    print(grade)
elif 80<marks<100:
    print("B+")
elif 60<marks<80:
    print("C+")
else:
    print("Student has failed")