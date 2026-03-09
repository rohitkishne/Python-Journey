# input() - this function take data from the user during program execution
# it takes the user type and save it as a string(text) by default
# Input and Type Casting
# name = input("Enter your name:")
# print("welcome ",name)

# Input problem - always takes the value but convert it into string
# age = input("Type age :")
# age = age + 5
# print(type(age))
# print("Your age is",age)

# Input Solution - TypeCasting - change data type forcibly ex text --> number 
# TypeCasting python built in function -
# int() - integer number
# float() - decimal number
# str() - text

# age = int(input("Type age :"))
# age = age + 5
# print(type(age))
# print("Your age is",age)

# convert number to string
# sales = 5000
# text = "Your sales is " + str(sales)
# print(text)

# Practice Assessment - Total Sales Calculator
# product = input("Product Name: ")
# quantity = int(input("Enter Your Quantity: "))
# price_per_unit = float(input("Enter price per unit: "))
# total_Sales = quantity * price_per_unit
# print("----------------------------------------")
# print("Product Name:",product)
# print("Total Sales:", total_Sales)

# Assignment - Salary slip calculator
Employee_Name = input("Enter Employee Name: ")
Basic_Salary = float(input("Enter Your Salary: "))
Bonus_Amount = float(input("Your Bonus: "))
Tax_percentage = int(input("Tax Applied: "))

# Calculation like gross salary, tax amount, net salary
Gross_Salary = Basic_Salary+ Bonus_Amount
Tax_Amount = (Gross_Salary * Tax_percentage)/100
Net_Salary = Gross_Salary - Tax_Amount

# printing all the instuction 
print("-------------------------------------------")
print("Employee Name:",Employee_Name)
print("Gross Salary of",Employee_Name, "is", Gross_Salary)
print("Tax Amount Applied on the salary of",Employee_Name, "is", Tax_Amount)
print("Net Salary of",Employee_Name, "is", Net_Salary)