# String Indexing and Slicing
# Forward vs Backword indexing
# Forward --> Left to Right
# Backward --> Right to Left
# EX :       S  H  Y  A  M
# Forward -  0  1  2  3  4
# Backward- -5 -4 -3 -2 -1

# String Indexing
# Example :
# name = "shyam"
# print(name)
# print(name[0])
# print(name[-5])
# print(name[-2])

# String Slicing
# Example :
# product = "Laptop pro 2026"
# print(product[0:6])
# print(product[-4:])

text = "DataAnalysis"
# Extract first 4 character
# print("First 4 character:",text[0:4])

# Extracting character from the middle to last
# print("Middle Slicing:", text[4:12])

# Extract till end
# print("Till end:", text[4:])

# Extract from beginning
# print("From Beginning:", text[:4])

# Extract last 5 character
# print("Last 5 character:", text[-5:])

text = "DataAnalysis"
# Skip Character between word
# print("Skip character in words till end:", text[0::2])
# print("Skip character in words:", text[::2])

# Reverse String
# print("Reverse order of text:", text[::-1])
# print("Reverse order of text:", text[::-2])
print("Reverse order of text:", text[:3:-1])
print("Reverse order of text:", text[3::-1])
