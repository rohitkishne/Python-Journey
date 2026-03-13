# Writing Clean Data to CSV
# Import CSV file
import csv
# # First Example --------
# # Clean Name (strip + title)
# cleaned_Name = []
# with open("Learning\Advance_Topics\practice.csv","r") as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     row["Name"] = row["Name"].strip().title()
#     cleaned_Name.append(row)
# # print(cleaned_Name) 

# with open("New_CleanedPractice_File.csv","w",newline="") as file:
#   writer = csv.DictWriter(file, fieldnames = reader.fieldnames)
#   writer.writeheader()
#   writer.writerows(cleaned_Name)
# print("File has been created with cleaned Name : New_CleanedPractice_File.csv ")


# Second Example ----------

# Correct City Names Map
# city_name = {
#   "mombai" : "Mumbai",
#   "kolcata" : "Kolkata",
#   "delhii" : "Delhi"
# }

# output = []
# with open("D:\Excels Project\Python\Learning\EmployeeData.csv", "r") as file:
#   reader = csv.DictReader(file)
#   for row in reader:
#     c = row["City"].strip().title()
#     row["City"] = city_name.get(c.lower(),c) #Correct the names of city through mapping
#     output.append(row)
# # print(output)

# with open("Correct_City_Name_File.csv","w",newline="") as f:
#   writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
#   writer.writeheader()
#   writer.writerows(output)
# print("Mapping Completed! : File generated with the name of Correct_City_Name_File.csv")


mumbai_sales = []
with open("Correct_City_Name_File.csv", "r") as f:
  reader = csv.DictReader(f)
  for row in reader:
    if row["City"].strip().lower() == "mumbai":
      mumbai_sales.append(row)
# print(mumbai_sales)

with open("Mumbai_Sales_Data.csv","w", newline="") as file:
  writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
  writer.writeheader()
  writer.writerows(mumbai_sales)
print("Mumbai Sale Data file has been created with the name of Mumbai_Sales_Data.csv")
