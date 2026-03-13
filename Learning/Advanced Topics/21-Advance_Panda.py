# Advance Pnada Function 
import pandas as pd

# Load cleaned employee data
df = pd.read_csv("CleanDataPracticeFile.csv")
# print("Data Loaded -----------------------------------")
# print(df)

# Multiple Condition
# Advance Filtering
# And (&) - Both Condition must true
# Data_by_sales_and_region = df[(df["Region"]=="North") & (df["Sales"]>500)]
# print(Data_by_sales_and_region)

# OR (|) - Either condition will be true
# Data_by_sales_and_region = df[(df["Region"]=="North") | (df["Sales"]>500)]
# print(Data_by_sales_and_region)

# Using isin() --> it allows us to create a filter list inside dataframe as per different criteria
# Employees_Electronics_Furniture = df[df["Category"].isin(["Electronics","Furniture"])]
# print(Employees_Electronics_Furniture)

# Advance Sorting
# Sorting_by_Region_Sales = df.sort_values(["Region","Sales"], ascending=[True,False])
# print(Sorting_by_Region_Sales)

# Group By operation
# sales_Stats = df.groupby("Region")["Sales"].agg(["min","max","mean","count"])
# print(sales_Stats)

# Sorting with Grouping
avg_Sales = df.groupby("Region")["Sales"].sum()
# print(avg_Sales)
# sort_Avg_Sales = avg_Sales.sort_values(ascending=False)

# print(sort_Avg_Sales)
