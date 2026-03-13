# Pandas Library in Python
# Used For Data Manipulation and analysis, fast and flexible, expensive Data structure
# Two type storage in Panda
# 1) Series - 1-D labeled Array
# 2) DataFrame - 2-D like Structure
# Built on top of NumPy
# It is like Excel in Python --> 1000x times powerful ---> Handles millions of rows easily
# Pandas = Panel + Data
# ---------------------------------------------------------------------------------------------

# Import Panda
import pandas as pd

# Series - 1D labelled Array
# s = pd.Series([10,20,30])
# print(s)

# Datafrom - like a Excel Sheet

# Data = {
#   "Name" : ["Shyam","Ram"],
#   "Age" : [52,45]
# }

# df = pd.DataFrame(Data)
# print(df)

# Load the CSV file using Pandas
df = pd.read_csv(r"Learning\Advance_Topics\EmployeeData.csv")
print("------------------ Row Data ----------------------")
# print(df.head())  # head() ---- Top Five Record show by default
# print(df.tail())  # tail() ---- Bottom Five Record show by default

# Find Basic Information in data frame (df)
# Find Rows and Column Number - Shape function
# print("\nShapes:", df.shape)

# Column information - columns function
# print("\nColumnInfo:",df.columns)

# Full Information of data
# print(df.info())

# Describe function
# print("\n Descrition:",df.describe())

# -----------------------------------------------------------------------------

# Data Cleaning
# Clean Employee Names
# print("------------------ Output ----------------------")
df["Full Name"] = df["Full Name"].str.strip().str.title()
# print(df.head())

# Clean Dept name
# print("------------------ Output ----------------------")
df["Dept"] = df["Dept"].str.strip().str.upper()
# print(df.head())

# Combine Output
# print("------------------ Column wise Combine Output ----------------------")
# print(df[["Full Name","Dept"]].head())

# Removes Duplicates
# print(df)
# print("\nDuplicate Rows:", df.duplicated().sum())
# df = df.drop_duplicates()
# print("------------------ Output ----------------------")
# print(df)

# Filter Data
# Employees from IT Dept
# it_Dept = df[df["Dept"].str.lower().str.strip()=="it"]
# print(it_Dept)

# # Employees whose salary is more than 60000
# df["Annual_Salary"] = pd.to_numeric(df["Annual_Salary"], errors='coerce')
# salary = df[df["Annual_Salary"]>60000]
# print(salary)

# print("Employees Salary > 60000:", salary.shape[0]) # Information about rows --> Shape[0]
# print("Employees Salary > 60000:", salary.shape[1]) # Information about column --> Shape[1]

# Sorting Data using Pandas
# Sort Data by Salary
# print(df)
# df["Annual_Salary"] = pd.to_numeric(df["Annual_Salary"].str.strip(), errors="coerce")
# df_sort_salary = df.sort_values("Annual_Salary",ascending=False)
print("-------------------------output--------------------")
# print(df)

# df["Annual_Salary"] = pd.to_numeric(df["Annual_Salary"].str.strip(), errors="coerce")
# df["Annual_Salary"] = df["Annual_Salary"].fillna(0)
# df_sort_salary = df.sort_values("Annual_Salary", ascending=True)
# print(df)

# Sort by Date
# df_sorted_date = df.sort_values("JoinDate") 
# print(df_sorted_date)

# Adding New Column
# Department Catergory created on the basis of dept and categorize them differently using lambda
# df["DepartmentCategory"] = df["Dept"].apply(
#   lambda x : "Category A" if x == "IT" else "Category B" if x == "MARKETING" 
#   else "Category C" if x == "HR" else "Category C"
# )
# print(df)

# Experience year created on the basis of experience and dont categorize
# df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors="coerce")
# df["Experience"] = 2025-df["JoinDate"].dt.year # Find out the year from the date
# print(df)

# Group by function
# Average salary by department
# Avg_salary_department_Wise = df.groupby("Dept")["Annual_Salary"].mean()
# print(Avg_salary_department_Wise)

# Total Salary by city
# totalCitySalary = df.groupby("City")["Annual_Salary"].sum()
# print(totalCitySalary)

# Employee count by Department
# count_dept = df.groupby("Dept")["ID"].count()
# print(count_dept)

# Export Clean Data -
# Selected_Column = df[["ID","Full Name","Dept"]]
# Selected_Column.to_csv("Selected_Column_file.csv", index=False)
# print("File has been Created")
