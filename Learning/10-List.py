# List
# Create List
# fruits = ["Banana","Mango","Orange"]
# print(fruits)

# Indexing
# print(fruits[0])
# print(fruits[-1])

# Update List 
# fruits[1] = "Apple"
# print(fruits)

# Add items into list
# fruits.append("Grapes")
# print(fruits)

# Insert items into perticular position
# fruits.insert(1, "Mango")
# print(fruits)

# Remove items from list - name the date to remove items
# fruits.remove("Mango")
# print(fruits)

# pop(remove) items - taking index to remove, by default removes from last index
# fruits.pop(0)
# print(fruits)

# Slicing in list
numberList = [0,24,6,78,45,40]
# print(numberList[0:3])
# print(numberList[:3])
# print(numberList[-3:])

# Looping in list
# for i in numberList:
#   print(i)

# Clean the cities
# cities = ["Mumbai  ","DelhI", " Agra"]
# cleanCities = []
# for c in cities:
#   formatingCity = c.strip().title()
#   cleanCities.append(formatingCity)
# print(cleanCities)

# Replace in list
# wrongCityName = ["calcutta", "Bombay"]
# rightCityName = []
# for city in wrongCityName:
#   city = city.replace("calcutta","Kolkata").replace("Bombay","Mumbai")
#   rightCityName.append(city)
# print(rightCityName)

# Extract year from list
# codes = ["Laptop-2023","honda-2025"]
# years = []
# for y in codes:
#   years.append(y[-4:])
# print(years)

# # Concatenate two Tuples
# a = (1,2)
# b = (3,4)
# print(a+b)

# Packing and unpacking
# data = ("Laptop",45000,"Black")
# product, price, color = data
# # print(product, price, color)
# # format string usecase
# print(f"Product : {product}, Price : {price} and Color : {color}")

# Nested Tuples inside List
# Employees = [("E101", "Shyam","Mumbai"),("E102","Radha","Delhi")]
# for eid, name, location in Employees:
#   print(eid, name, location)