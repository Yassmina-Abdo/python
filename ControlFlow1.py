# ------------------------------
# Control Flow
# if -  elif  -  else
# Make Descision
# ------------------------------


# uName = "Abdelrahman"
# cName = "Python Course"
# cPrice = 100
# cDiscount = 30
# print(f"Hello \"{uName}\" The \"{cName}\" price is \"${cPrice-cDiscount}\"")


# ---------------------------------------------------------------------------
# uName = "Abdelrahman"
# country = "USA"
# cName = "Python Course"
# cPrice = 100

# if country == "Egypt":
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-80}\"")
# elif country == "KSA":
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-40}\"")
# elif country == "Sudan":
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-90}\"")
# else:
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-25}\"")

# ---------------------------------------------------------------------------
# uName = "Abdelrahman"
# country = "KSA"
# cName = "Python Course"
# cPrice = 100
# # Assume egypt and sudan should have the same discount, Also KSA and Qatar
# if country == "Egypt" or country == "Sudan":
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-80}\"")
# elif country == "KSA" or country == "Qatar":
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-40}\"")
# else:
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-25}\"")

# ---------------------------------------------------------------------------
# uName = "Abdelrahman"
# country = "Qatar"
# cName = "Python Course"
# cPrice = 100
# isStudent = False
# # if the user is a student make bigger discount
# if country == "Egypt" or country == "Sudan":
#     if isStudent:

#         print(
#             f"Hello \"{uName}\" because you are from \"{country}\" and student")
#         print(f"The \"{cName}\" price is \"${cPrice-90}\"")
#     else:

#         print(f"Hello \"{uName}\" because you are from \"{country}\"")
#         print(f"The \"{cName}\" price is \"${cPrice-80}\"")

# elif country == "KSA" or country == "Qatar":
#     if isStudent:

#         print(
#             f"Hello \"{uName}\" because you are from \"{country}\" and student")
#         print(f"The \"{cName}\" price is \"${cPrice-60}\"")
#     else:

#         print(f"Hello \"{uName}\" because you are from \"{country}\"")
#         print(f"The \"{cName}\" price is \"${cPrice-40}\"")
# else:
#     if isStudent:

#         print(
#             f"Hello \"{uName}\" because you are from \"{country}\" and student")
#         print(f"The \"{cName}\" price is \"${cPrice-45}\"")
#     else:

#         print(f"Hello \"{uName}\" because you are from \"{country}\"")
#         print(f"The \"{cName}\" price is \"${cPrice-25}\"")

# ---------------------------------------------------------------------------
# uName = "Abdelrahman"
# country = "Egypt"
# cName = "Python Course"
# cPrice = 100
# countryList1 = ["Egypt", "Sudan", "Algeria", "Syria"]
# countryList2 = ["Qatar", "KSA", "UAE"]
# if country in countryList1:
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-80}\"")
# elif country in countryList2:
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-40}\"")
# else:
#     print(f"Hello \"{uName}\" because you are from \"{country}\"")
#     print(f"The \"{cName}\" price is \"${cPrice-20}\"")


# ---------------------------------------------------------------------------
# Short way for if (Ternary if)
# [statement_on_True] if [condition] else [statement_on_false]
# ---------------------------------------------------------------------------
movieRate = 18
age = 15

# if age < movieRate:
#     print("Movie isn't good for you")
# else:
#     print("Happy watching")
# if Format on save is off you can write the if statements in this way
# if age < movieRate:print("Movie isn't good for you")
# else:print("Happy watching")

# English Not programming ^_^
# print("Movie isn't good for you" if age < movieRate else "Happy watching")
# print("Movie isn't good for you") if age < movieRate else print("Happy watching")

# ---------------------------------------------------------------------------
# Find the minimum number
# ---------------------------------------------------------------------------
# a, b = 10, 20
# min = a if a < b else b
# print(min)

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
# if [a<b] is true it return 1, so element with 1 index will print
# else if [a<b] is false it return 0, so element with 0 index will print
# ---------------------------------------------------------------------------
# a, b = 70, 50
# print((b, a)[a < b])

# Use Dictionary for selecting an item
# if [a < b] is true then value of True key will print
# elif [a<b] is false then value of False key will print
# ---------------------------------------------------------------------------
# a, b = 90, 200
# print({True: a, False: b}[a < b])

# nested ternary operator
# ---------------------------------------------------------------------------
# a, b = 50, 20
# print("Both a and b are equal" if a ==
#       b else "b is the smaller than a" if a > b else "a is the smaller than b")

# if a == b:
#     print("Both a and b are equal")
# else:
#     if a > b:
#         print("b is the smaller than a")
#     else:
#         print("a is the smaller than b")


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in myList:
#     if number == 3:
#         continue
#     print(number)
# print("="*54)
# for number in myList:
#     if number == 8:
#         break
#     else:
#         print(number)

# for number in myList:
#     pass
# print("="*54)

# x = input("Please enter a symbol: ")
# c = chr(int(x))
# print(x, c)
# print("- _")

# ord ()  chr()


# write a program will find all such numbers
# which is divided by 7 but are not a multiple of 5
# between (2000,3000) both numbers are included
# The numbers should be printed in a comma seprated
# sequence on a single line

# string = "Abdelrahman@m"
# s2 = string.replace("@", "")
# print(s2)

# @domain.com
# [A-Z][a-z][0-9][@ or _][>=8]
password = "Abdelrahman44_"
specialchar = ["@", "#", "%", "$", "*", "&", "_"]
value = True
if len(password) < 8:
    print("Password Length is less than 8")
    value = False
if not any(char.isdigit() for char in password):
    print("Password should have at least one digit")
    value = False
if not any(char.isupper() for char in password):
    print("Password should have at least one uppercase")
    value = False
if not any(char.islower() for char in password):
    print("Password should have at least one lowercase")
    value = False
if not any(char in specialchar for char in password):
    print("Password should have at least one special char")
    value = False
if value:
    print("Valid Password")
