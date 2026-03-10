# For-Loop in Python
# Basic Loop
# for i in range(1,11):
#   print(i)

# # Print characters
# word = "python"
# for letters in word:
#   print(letters)

# word2 = "Sql"
# for i in range(1,6):
#   print(word2)

# Loop in list
# fruits = ["Apple", "Banana", "Mango"]
# for i in fruits:
#   print(i)

# Loop Even Numbers
# for i in range(1,21,2):
#   print(i)

# Total calculation
# marks = [40,50,10]
# total = 0
# for i in marks:
#   total += i
#   print("Total:",total)
# print("Final Total:", total)

# Clean city name
# city = ["MUMbai  ","  DelhI", "agra"]
# cleaned_city = []
# for i in city:
#   cleaned_city.append(i.strip().title())
#   print("What added:",cleaned_city)
# print("Final List of City:", cleaned_city)

# Loop with if condition
# number_List = [1,8,10,90,18,2]
# for i in number_List:
#   if i > 10:
#     print(i,"- This number is greater than 10")
#   else:
#     print(i,"- This number is smaller than 10")

# Check even or odd number in list
# number_is = [5, 9, 10, 7, 6, 14]
# for i in number_is:
#   if i%2==0:
#     print(i," is the even number")
#   else:
#     print(i," is the odd number")

# Extract last digit from IDs
# ids = ["EMP-1234","EMP-5678"]
# numberList = []
# alphaList = []
# for id in ids:
#   index = id.find("-")
#   numberList.append(id[index+1:])
#   alphaList.append(id[:index])
#   print(id[:index])
#   print(id[index+1:])
# print(numberList)
# print(alphaList)

# Extract last four digit from ID
# emp_id = ["emp001111","emp005648"]
# for i in emp_id:
#   print(i[-4:])

# Looping through Dictionary
# student = {
#   "name": "Shyam",
#   "age": 20,
#   "course": "B.Tech"
# } 

# for key, value in student.items():
#   print(key,":",value)

# -----------------------------------------------------------------------------------------------------------------------

# While Loop in Python
# i = 1
# while i<=5:
#   print(i)
#   i+=1

# Countdown
# n = 5
# while n>0:
#   print(n)
#   n-=1

# Ask user a number until valid Input
# number = ""
# while not number.isnumeric():
#   number = input("Enter Any number: ")
# print("Number is Valid and Accepted")

# Loop through list using while
# print(len(items))
# items = ["Apple","Banana","Mango"]
# i = 0
# while i < len(items):
#   print(items[i])
#   i+=1

# Break Condition
# x = 1
# while x<=10:
#   if x==5:
#     break
#   print(x)
#   x+=1

# Continue Condition ---> if the continue condition satify, it redirect to start without running code below continue 
# n = 0
# while n < 10:
#   if n%2==0:
#     n+=1
#     continue
#   print(n)
#   n+=1
# -----OR-----
# n = 0
# while n < 10:
#   n+=1
#   if n%2==0:
#     continue
#   print(n)
 
# Password System Assessment
passwd = ""
attempt = 0
while passwd!="admin123" and attempt < 3:
  passwd = input("Enter Admin Password: ")
  attempt+=1
  if passwd!="admin123":
    print("Wrong Password, This is your", attempt,"Attempt")
if passwd!="admin123":
  print("You are Blocked")
else:
  print("Access Granted")
  
 
  
