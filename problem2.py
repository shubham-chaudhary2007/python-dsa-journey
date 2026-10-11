#Take input of a student's name, age, percentage, and pass/fail status. Print each value with its data type.

name=(input("Enter your name:-"))

age=int(input("Enter your age:-"))

percentage=float(input("Enter your percentage:-"))

passed= percentage >= 35



print("Name:",name + "  Data Type:-",type(name))

print("Age:",age ,"  Data Type:-",type(age))

print("Percentage:",percentage, "  Data Type:-",type(percentage))

print("pass:",passed ,"  Data Type:-",type(passed))
