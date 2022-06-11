# -------------------
# Concatenation --
# -------------------

# name = input(" Please Enter your name")
# id = 777
# msg = "Hello,"
# fullMsg = msg + " " + name + " and your id is: "
# print(fullMsg)
# print(fullMsg + id)  # Error can only concatenate str (not "int") to str

# --------------------------------
# Indexing -- Slicing
# Note: Python use zero Indexing
# --------------------------------
myString = "I Love Python"

print(myString[3])  # index 3 => prints 'o'
print(myString[10])  # index 10 => prints 'h'
print(myString[-1])  # index -1 => prints 'n'

#slicing [start:end]
print(myString[0:5])  # index 0 to 5 => prints 'I Lov'
print(myString[0:6])  # index 0 to 6 => prints 'I Love'
print(myString[:6])  # index 0 to 6 => prints 'I Love'
print(myString[2:6])  # index 2 to 6 => prints 'Love'
print(myString[2:7])  # index 2 to 7 => prints 'Love '
print(myString[2:13])  # index 2 to 13 => prints 'Love Python'
print(myString[2:])  # index 2 to 13 => prints 'Love Python'
print(myString[1:-1])  # index 1 to -1 => prints ' Love Pytho'

#slicing [start:end:step]
print(myString[0:5:2])  # index 0 to 5 with step 2 => prints 'ILv'
print(myString[2:13:3])  # index 0 to 5 with step 2 => prints 'Leyo'
