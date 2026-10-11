#Take input of your BOD and current date. Print your approximate age using variables

date=int(input("Enter Your date on BOD:-"))

month=int(input("Enter Your Month on BOD:-"))

year=int(input("Enetr Your Year on BOD:-"))



#asking user to enter curret date to calculate there age 

print("Enter Today Date,Month,Year")

cur_date=int(input("Enter Today Date:-"))

cur_month=int(input("Enter Today month:-"))

cur_year=int(input("Enter Today Year:-"))



#below code used to calculate the age 

cal_year=int(cur_year - year)

cal_month=int(cur_month - month)

cal_date= int(cur_date - date)

print("Your approximate age is:")

print(cal_year,"Year ", cal_month, "Months ", cal_date,"Date")
