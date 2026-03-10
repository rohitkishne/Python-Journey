# Dictionary Creation
student = {
  "name": "Shyam",
  "age": 29,
  "city": "kolkata"
}
# print(student)

# Access values in dictionary
# print(student["name"])
# print(student["age"])
# print(student["city"])

# # Adding and Modifying dictionary
# # Add
# student["marks"] = 85
# # Modify
# student["city"] = "Mumbai"
# print(student)

# Remove
# student.pop("age")
# print(student)

# Dictionary Methods
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("name"))
# print(student.get("age"))
# print(student.get("city"))

# Looping in Dictionary
# for k in student:
#   print(k, student[k])

# Nested Dictionary
# Employees = {
#   "E01" : {"name":"Shyam","age":29,"city":"agra"},
#   "E02" : {"name":"Arun","age":20,"city":"kolkata"}
# }
# print(Employees)
# print(Employees["E02"]["name"])
# print(Employees["E02"]["age"])
# print(Employees["E02"]["city"])

# # Mapper Wrong --> Correct
# mapper = {
#   "mombai" : "Mumbai",
#   "calcutta": "Kolkata"
# }
# print(mapper["mombai"])
# print(mapper["calcutta"])