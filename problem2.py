#Take input of a student's name, age, percentage, and pass/fail status. Print each value with its data type.

name=str(input("Enter your name:-"))

age=float(input("Enter your age:-"))

percentage=float(input("Enter your percentage:-"))


print("Name:",name + "  Data Type:-",type(name))

print("Age:",age ,"  Data Type:-",type(age))

print("percentage:",percentage ,"  Data Type:-",type(percentage))


if percentage >= 35:
    print("Pass")
else:
    print("Fail")

