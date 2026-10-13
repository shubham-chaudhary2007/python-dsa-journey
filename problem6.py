#Take a student's marks as input.
#Print 'Distinction' for marks of 75 or above,
#'First Class' for 60–74, 
#'Second Class' for 40–59, 
#and 'Fail' below 40.
#Reject marks outside the range 0–100.



mark=float(input(" Enter your mark:-"))

if mark <0 or mark >100:
    print("enter valid marks form 0 to 100")
elif mark >=75:
    print("Distiction")
elif mark >=60:
    print("Fisrt calss")
elif mark >=40:
    print("second class")
else:
    print("Fail")