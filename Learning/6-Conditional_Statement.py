# If-else Condition
# Use-Case - Filter Data, Validate Inputs, Categorize Values

# age = int(input("Enter Your AGE:"))

# if age>=18:
#   print("Adult")
# else:
#   print("Young")

# Discount Case
# amount = 1400
# if amount>=1500:
#   print("Take a discount")
# else:
#   print("Put a more Effort to get a discount")

# if-elif-else ---> Multiple condition scenerio
# marks = int(input("Enter your marks: "))

# if marks>=75:
#   print("A")
# elif marks >=50:
#   print("B")
# elif marks>=30:
#   print("C")
# else:
#   print("Fail")

# String Based condition - Be careful as python is case sensitive
# Ex: Password Validation
# Password = input("Enter Your Password: ") ---> Dont use lower() in case of password, 
#                                        because giving access to someone must match the password

# if Password == "Admin@123":
#   print("Login Successful")
# else:
#   print("Wrong Credentials")

# Found the city with lower()
# city = "Delhi"
# if city.lower() == "delhi":
#   print("You are on Right path")
# else:
#   print("You take the wrong turn")

# Email Validation
# email = "student@gmail.com"

# if "@" in email and "." in email:
#   print("Valid Email")
# else:
#   print("Enter Valid Email")

# Advanced: Missing Data Check
# value = ""
# if value == "":
#   print("Missing Data Found")
# else:
#   print("Everything is fine")

# Nested if and Multiple Condition
# year = int(input("Enter Year: "))

# if year%4==0:
#   if year%100==0 and year%400!=0:
#     print("Year is not a Leap Year")
#   else:
#     print("Year is a Leap Year")
  
# else:
#   print("Year is not a Leap Year")

# check even and odd number
# numb = int(input("Enter Number: "))

# if numb%2==0:
#   print("Even Number")
# else: 
#   print("Odd Number")

# Club Entry Checkpoint

# age = int(input("Enter Your Age: "))
# if age>=18:
#   id_num = int(input("Enter Your ID: "))
#   if id_num == 1234:
#     print("Now! You can go to club")
#   else:
#     print("Your id is not valid")
# else:
#   print("You are underage for Club")

# Assessment - Confidential Meeting room Entry
# Security_code = int(input("Enter Security Code : "))
# if Security_code == 5566:
#   department = input("Enter Your Department: ")
#   if department.lower() == "finance" or department.capitalize()=="Finance" or department.upper() == "FINANCE":
#     access_level = int(input("Enter Your Access_Level: "))
#     if access_level >=5:
#       print("Access Granted: Welcome to the Meeting Room")
#     else:
#       print("Insufficient Access Level")
#   else:
#     print("Access Denied: Department not Allowed")
      
# else:
#   print("Invalid Security Code")

# Assignment - online Exam Login
Reg_No = int(input("Enter Your Registration Number : "))
if Reg_No == 1234:
  subject = input("Enter Your Subject : ")
  if subject.capitalize() == "Python" or subject.upper() == "PYTHON" or subject.lower() == "python":
    passwd = int(input("Enter Your Password : "))
    if passwd == 8888:
      print("Login Successful! Start Your Exam")
    else:
      print("Wrong Password")
  else:
    print("Subject Not Available")
else:
  print("Registration failed")