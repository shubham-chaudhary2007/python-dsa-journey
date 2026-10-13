#Ask the user for their age and citizenship status. 
#Allow them to vote only if they are at least 18 years old and are a citizen.


age=int(input("enter your age to vote:"))
citizen = input("are you citizen? (yes/no)").lower()


if age >=18 and citizen == "yes":
    print(" you are eligiable to vote")
else:
    print("you can't vote")