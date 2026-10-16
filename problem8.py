#Create a login check using a username and password. 
#Allow access only if both match the predefined credentials.


# username and password which is alredy store in database

user_DB="subam01"
pass_DB="subam2007"



user_log=input("Enter your Username:").lower()
pass_log=input("Enter your Password:")

if user_log == user_DB and pass_log == pass_DB:
    print("Welcome back to your Account")
else:
    print("Both Username and Password are invalid")
