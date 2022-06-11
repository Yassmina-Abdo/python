# ---------------------------------------------------------------------
# Functions
# [1] A function is a reusable block of code to do a task
# [2] A function run when you call it
# [3] A function accepts elements to deal with called parameter
# [4] A function can do a task without returning data
# [5] A function can return data after job is finished
# [6] A function is made to prevent DRY ("Don't repeat yourself")
# [7] A function Accepts elements when you call it called Arguments
# [8] There're built in functions and user defined functions
# [9] A function is made for all team and apps
# ---------------------------------------------------------------------


def function_name():
    print("Hello from this function")


def function_name2():
    return "Hello from this function"

# ---------------------------------------------------------------------


# Function parameter and arguments
# a, b, c = "Abdelrahman", "Hossam", "Sobhy"
# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")

# def                     ===> Function keyword Define
# Hello_msg               ===> Function Name
# name                    ===> Parameter
# print(f"Hello {name}")  ===> Task "Implementation"
# Hello_msg("Abdelrahman")===> Abdelrahman is argument


# def Hello_msg(name):
#     print(f"Hello {name}")


# Hello_msg(a)
# Hello_msg(b)
# Hello_msg(c)

# ---------------------------------------------------------------------

# def addition(num1, num2):
#     return num1 + num2


# print(addition(100, 200))
# ---------------------------------------------------------------------
# Function packing and unpacking Arguments *Args

# print(1, 2, 3, 4)
# myList = [1, 2, 3, 4]
# print(myList)
# print(*myList)


# def Hello_msg(n1, n2, n3, n4):
#     pass


# people = [n1, n2, n3, n4]
# for name in people:
#     print(f"Hello {name}")
# This will case a problem because number of I/Ps is more than required
# TypeError: Hello_msg() takes 4 positional arguments but 5 were given
# Hello_msg("Abdelrahman", "Hossam", "Sobhy", "Ibrahim", "Abdo")
# ---------------------------------------------------------------------

# def Hello_msg(*people):  # n1 , n2, n3, n4
#     print(people)
#     for name in people:
#         print(f"Hello {name}")


# Hello_msg("Abdelrahman", "Hossam", "Sobhy", "Ibrahim", "Abdo")
# Hello_msg("Abdelrahman", "Ali")

# ---------------------------------------------------------------------

# before packing and unpacking
# def Show_Skills(n1, n2, n3):
#     print(f"{n1}")
#     print(f"{n2}")
#     print(f"{n3}")


# Show_Skills("c", "Java", "Python")


# def Show_Skills(*skills):
#     for skill in skills:
#         print(f"{skill}")


# Show_Skills("c", "Java", "Python", "PS")
# Show_Skills()
# ---------------------------------------------------------------------

# def Show_Skills(name, *skills):
#     print(f"Hello,{name} Those are your skills")
#     for skill in skills:
#         print(f"{skill}")


# Show_Skills("Abdelrahman")
# Show_Skills("c", "Java", "Python", "PS")
# Show_Skills("Abdelrahman", "c", "Java", "Python", "PS")
# ---------------------------------------------------------------------

# note the *
# def Show_Skills(name, *skills):
#     print(f"Hello,{name} Those are your skills")
#     for skill in skills:
#         print(f"{skill}")


# x = ["c", "Java", "Python", "PS"]
# Show_Skills("Abdelrahman", *x)


# def Show_Skills(name, skills):
#     print(f"Hello,{name} Those are your skills")
#     for skill in skills:
#         print(f"{skill}")


# x = ["c", "Java", "Python", "PS"]
# Show_Skills("Abdelrahman", x)
# ---------------------------------------------------------------------

# Function Default Parameters


# def Hello_msg(name, age, country):
#     print(f"Hello,{name} your age is {age} and your country is {country}")


# Hello_msg("Abdelrahman", 25, "Egypt")
# Hello_msg("Mohamed", 17, "KSA")
# # Hello_msg("Ali", 20,)  # will get an error

# How to solve ?


# def Hello_msg(name, age, country="UnKnown"):
#     print(f"Hello,{name} your age is {age} and your country is {country}")


# Hello_msg("Abdelrahman", 25, "Egypt")
# Hello_msg("Mohamed", 17, "KSA")
# Hello_msg("Ali", 20,)
# ---------------------------------------------------------------------
# note the error becaues if first var has initial value all the
# others should also have one


# def Hello_msg(name="UnKnown", age, country="UnKnown"):
#     print(f"Hello,{name} your age is {age} and your country is {country}")


# Hello_msg("Abdelrahman", 25, "Egypt")
# Hello_msg("Ali", 20,)
# ---------------------------------------------------------------------

# Function packing and unpacking Arguments **KWArgs

# def Show_Skills(*skills):
#     print(type(skills))
#     for skill in skills:
#         print(f"{skill}")


# Show_Skills("c", "Java", "Python", "PS")
# ---------------------------------------------------------------------
# def Show_Skills(**skills):
#     print(type(skills))
#     for skill, value in skills.items():
#         print(f"{skill} ===> {value }")


# Show_Skills(C="80%", Java="65%", Python="90%", PS="70%")
# ---------------------------------------------------------------------
# def Show_Skills(**skills):
#     print(type(skills))
#     for skill, value in skills.items():
#         print(f"{skill} ===> {value }")


# myDict = {
#     "C": "80%",
#     "Java": "65%",
#     "Python": "90%",
#     "PS": "70%"
# }
# # Show_Skills(myDict)  # Error because unpacked
# Show_Skills(**myDict)
# ---------------------------------------------------------------------
# def show_Skills(name, *skills, **skills2):
#     print(f"Hello,{name} your skills: ")
#     for skill in skills:
#         print(f"- {skill}")
#     for skill, progress in skills2.items():
#         print(f"- {skill} ===> {progress}")


# show_Skills("Abdelrahman", "C", "Java", "Assembly", python="70%")
# ---------------------------------------------------------------------
# def show_Skills(name, *skills, **skills2):
#     print(f"Hello,{name} your skills: ")
#     for skill in skills:
#         print(f"- {skill}")
#     for skill, progress in skills2.items():
#         print(f"- {skill} ===> {progress}")


# myDict = {
#     "Id": "80%",
#     "AE": "65%",
#     "Python": "90%",
#     "PS": "70%"
# }
# myTuple = ("C", "Java", "Assembly")
# show_Skills("Abdelrahman", *myTuple, **myDict)
# ---------------------------------------------------------------------

# Function Scope

# x = 1  # global Scope


# def printf():
#     print(f"This value from function scope {x}")


# print(f"This value from global scope {x}")
# printf()

# ---------------------------------------------------------------------
# Error in the scope of x
# def printf():
#     x = 1
#     print(f"This value from function scope {x}")


# print(f"This value from global scope {x}")
# printf()

# x = 1  # global Scope

# ---------------------------------------------------------------------
# x = 1


# def printf():
#     x = 2
#     print(f"This value from function scope {x}")


# print(f"This value from global scope {x}")
# printf()
# ---------------------------------------------------------------------
# x = 1


# def printf():
#     x = 2
#     print(f"This value from function scope 1 :{x}")


# def printf2():
#     x = 4
#     print(f"This value from function scope 2 :{x}")


# print(f"This value from global scope {x}")
# printf()
# printf2()
# print(f"This value from global scope {x}")
# ---------------------------------------------------------------------
# x = 1


# def printf():
#     global x
#     x = 2
#     print(f"This value from function scope 1 :{x}")


# def printf2():
#     x = 4
#     print(f"This value from function scope 2 :{x}")


# print(f"This value from global scope {x}")
# printf()
# printf2()
# print(f"This value from global scope after function is called {x}")
# ---------------------------------------------------------------------

# lambda Function
# [1] It has no Name
# [2] You can call it Inline without defining it
# [3] you can use it in return data from another function
# [4] lambda used for simple function and def for large function
# [5] lambda is one single expression not block of code
# [6] lambda type is a function

# def say_Hello(name):
    return f"Hello {name}"


# def hello(name): return f"Hello {name}"


# print(say_Hello("Abdelrahman"))
# print(hello("Abdelrahman"))

# x = lambda y : y + 7
# print (x(5))

# z = lambda a, b : a > b
# print (z(3,7))
