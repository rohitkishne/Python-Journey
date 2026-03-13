# File Handling using Python

# # Read Files 
# with open("sampletext", "r") as f:
#   print(f.read())

# Read file line by line
# with open("sampletext","r") as f:
#   for text in f:
#     print(text.strip().title())

# Write file, if file available or not, it creates if it is not there
# with open("newText","w") as file:
#   file.write("Hi, its new file\n")
#   file.write("This is second line\n")

# Append a new line
# with open("newText","a") as newText:
#   newText.write("This is third line\n")

# Clean Data in file
# cleaned = []
# with open("sampleText","r") as f:
#   for line in f:
#     cleaned.append(line.strip().title())
# print(cleaned)

# with open("cleanedFile","w") as file:
#   for city in cleaned:
#     file.write(city +"\n")

# Counting Lines
# count = 0
# with open("cleanedFile", "r") as file:
#   for _ in file: '''-------> Underscore(_) used here, that represents the each line/row, while looping it counts each line'''
#     count+=1
# print("Total Lines:",count)