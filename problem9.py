#Take a person's age and monthly income as input.
#Approve a loan only if the person is at least 21 years old and earns
#at least ₹25,000 per month.

age=int(input("Enter your age:"))
income=float(input("Enter your monthly income:"))
loan=float(input("enter your loan Amount:"))

if age >=21 and income >=25000:
    print("Loan Amount ₹",loan,"is approved")
elif age < 21 and income < 25000:
    print("Your age is below 21 and Your are income is below ₹25000 you can't get loan")
elif age <21:
    print("Your age is below 21 you can't get loan")
else:
    print("income is below ₹25000 you can't get loan")