# Function in Python

# Defined function with any parameter/arguments
# def greet():
#   print("Hello World")
# greet()

# # Defined function with parameter and arguments
# def welcome(name):
#   print("Welcom",name)
# welcome("Shyam")

# Argument vs parameter
# Argument - assigning a value inside function during calling
# Parameter - defined a variable inside function while creating, pass as a placeholder for the data as input

# # Add function
# def add(a,b):
#   print("a+b:",a+b)
# add(5,5)

# Return instead of printing - Help in saving the function output inside new variable and can be use further in code
# but we can not do so with print, because it is not store somewhere, it directly prints data.
# def add(a,b):
#   return a+b
# Addition = add(5,6)
# print("Addition:",Addition)

# Return and function into function usecase
# def add(a,b):
#   return a+b

# def multiple(x):
#   return x*2

# result = multiple(add(5,4))
# print(result)

# # clean text function
# def clean_text(text):
#   return text.strip().title()

# CleanedText = clean_text(" MuMbai   ")
# print(CleanedText)

# # cleaning city
# def fix_city(city):
#   city = city.strip().lower()
#   city = city.replace("mombai","Mumbai")
#   city = city.replace("calcutta","Kolkata")
#   return city.title()

# print(fix_city("mombai"))

# # Get year from code
# def get_year(code):
#   return code[-4:]
# print(get_year("laptop-2025"))

# # Email validity checker function
# def Validate_email(email):
#   return "@" in email and "." in email
# print(Validate_email("student@gmail.com"))

# # Total salary
# def total_salary(salary,bonus):
#   return salary+bonus
# print(total_salary(5000,5000))

# # Different_output stats
# def stats(num):
#   return min(num), max(num), sum(num)
# print(stats([10,20,30]))


# Clean list return
# def cleanedList(fruits):
#   clean_list = []
#   for i in fruits:
#     clean_list.append(i.strip().title())
#   return clean_list

# print(cleanedList([" Apple"," MAngo ","banana  "]))
