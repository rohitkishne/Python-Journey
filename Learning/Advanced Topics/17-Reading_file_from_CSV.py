# Reading file from CSV
# Import csv
import csv

# Read Row wise data
# with open("Employee Sample Data.csv") as f:
#   reader = csv.reader(f)
#   for read in reader:
#     print(read)

# Read with DictReader - allowed column data extraction from the row
# with open("Employee Sample Data.csv") as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     print(row["EEID"], row["Full Name"], row["Department"])

# Total Sales
# Total = 0
# with open("Employee Sample Data.csv") as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     Total += int(row["Annual Salary"].replace("$",'').replace(",",'').strip())
    
# print("Total Salary:",Total) 

# Filter by city
Miami = []
with open("Employee Sample Data.csv") as f:
  reader = csv.DictReader(f)
  for row in reader:
    if row["City"]=="Miami":
      Miami.append(row)
print(Miami)

