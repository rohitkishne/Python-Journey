# Function of String, List and Number ---> Built-in Functions

# String functions
# count
# text = "banana"
# print(text.count("a"))

# Endswith
# print("hello.py".endswith(".py"))

# Startwith
# print("Sales.py".startswith("Sales"))

# value is digit
# print("123".isnumeric())
# # value is Alphabet
# print("ABC".isalpha())
# # value is Alpha-Numeric
# print("A1B2".isalnum())

# Split Lines
# print("Line1\nLine2")
# print("Line1\nLine2".splitlines())

# --------------------------------------------

# List Function
# sorting with number
# num = [6,8,3,1,4,0]
# num.sort()
# print(num)

# sorting with Text
# alpha = ["b","t","a","g","p"]
# alpha.sort()
# print(alpha)

# Min, Max, Sum
# marks = [10,20,30]
# print(min(marks))
# print(max(marks))
# print(sum(marks))

# Count and index in list
myList = [1,2,5,1,5]
# print(myList.count(1)) --> Count the occurence of value
# print(myList.index(5)) --> Count the index for value

# Extend function in list
# a = [1,2]
# b = [3,4]
# a.extend(b)
# print(a)


# -------------------------------------

# Number functions
# Round - give ciel value
# print(round(3.567,1))
# print(round(3.567,2))
# print(round(3.567,0))

# Absolute number
# print(abs(-50))

# Power
# print(pow(3,4))

# DivMod --> how many times value divide and remainder
# print(divmod(10,3))
# print(divmod(10,2))

# Sum
# print(sum([5,5,5],5))

# Cleaning Example:
# products = [" mobile","LaPtop ","    Knife"]
# clean = [p.strip().title() for p in products] -----> New Way of looping
# clean.sort()
# print(clean)

# # Email Example
# mails = ["rohit@gmail.com", "student@yahoo.com"]
# domains = [mail[mail.find("@")+1:] for mail in mails]
# print(domains)

# # Valid Mobile number
# mobiles = ["9876453135", "99955Bbb46", "12345","8796541230"]
# valid = [m for m in mobiles if m.isdigit() and len(m)==10]
# print(valid)