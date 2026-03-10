# String Methods 
# Use-Case : Cleaning, Formatting, Validation, Transformation

# Text = "          Hello Python Bro    "

# Remove spaces from text
# print("Remove spaces:",Text.strip())

# Text2 = "Hello Python Bro"

# Convert to UpperCase letters
# print("Capital letters:", Text2.upper())
# print("Capital letters:", Text.upper().strip())
# print("Capital letters:", Text.strip().upper())

# capitalize the word - only first letter of the first word is capitalize and other will be lowercase
# print("Capitalize the text2:", Text2.capitalize())

# Convert to proper case
# print("Proper Case:", Text2.title())

# Convert to LowerCase letters
# print("LowerCase letters:", Text2.lower())

# Replace text
# print("Replace python word   with sql:",Text2.replace("Python","SQL"))

# Count Letter Occurrence in word
# print("Count occurence of O:", Text2.count("o"))

# check whether text start with something
# print("Start with hello?", Text2.startswith("Hello"))

# Text3 = "965464131"
# check whether text start with number
# print("Is this numeric", Text3.isnumeric())

# msg = "Welcome to New Python World"

# Splits msg String into list of words
# words = msg.split()
# print("Word list:", words)

# Join with hiphen(-)
# joined_text = "-".join(words)
# print("Joined text with -:", joined_text)

Text2 = "Hello Python Bro"
# Find the position of letter
print("Find the pos of P:", Text2.find("P"))

# Email = "student@gmail.com"
# domain = Email[Email.find("@")+1:]
# print("Domain name:",domain)

# Assessment : Clean Price (Remove Special Characters)
# Example : "Price: $2500/-" --> "2500"
# price = "Price: $2500/-"
# Clean_Price = price.replace("Price:","")\
#                    .replace("$","")\
#                    .replace("/-","")\
#                    .strip()
# print("The final Clean Price is here:",Clean_Price)