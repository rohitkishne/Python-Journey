# NumPy Arrays and Data Cleaning in Python
# NumPy --> Used for Speed, Scientific and Mathematical Calculation in Vectorized form, deal with large dataset in speedy manner.  
# Fast as compare to python list as it stores data in array form with fixed datatypes
# import numpy
import numpy as np

# Creating Arrays using numpy
arr = np.array([10,20,30])
# print(arr)

# Indexing and Slicing
# print(arr[1]) #Indexing
# print(arr[-1])
# print(arr[0:2]) #Slicing


# # Vectorized Operations - calculate without loop
# print(arr+10) # Add in each number in array
# print(arr*10) # Multiply in each number in array
# print(arr**2) # Power in each number in array

# # NumPy Function
# print(arr.sum())
# print(arr.mean())
# print(arr.min(), arr.max())

# # Data Cleaning Example
# data = np.array([10,-20,70,80,63,-89,-42])
# clean = data[data>=0]
# print("Cleaned Data:",clean)/

# # Filled the number in place of negative values
# marks = np.array([10,-1,50,20,-1])
# marks[marks == -1] = marks[marks != -1].mean() #Average of non negative values 
# print("Filled Negative Values:", marks)

# Cleaning the data with text array
# cities = np.array([[" Mumbai ", "delhi  "," kolkata"]])
# cities = np.char.strip(cities)
# cities = np.char.title(cities)
# print(cities)

# Array with fixed Values
# zeroes = np.zeros(5)
# print(zeroes)
# ones = np.ones(5)
# print(ones)

# create array with range in numpy
# arr = np.arange(1,10)
# print(arr)

# # Random Array
# rand = np.random.randint(10,100,5) #take three values, (start, end and how many value we need )
# print(rand)

