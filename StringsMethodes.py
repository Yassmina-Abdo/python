# -------------------------
# String Methodes
# -------------------------

# length of string len()
# myString = "I Love Python"
# print(len(myString))

# strip()  -  rstrip()  -  lstrip()   Remove whitespaces
# myString = "     I Love Python   "
# print(myString.strip())
# print(myString.rstrip())
# print(myString.lstrip())

# title() - capitalize() - upper() - lower()
# myString = "I Love 2d and 3D graphics"
# print(myString.title())
# print(myString.capitalize())
# print(myString.upper())
# print(myString.lower())


# zfill() => Zero Fill
# a, b, c = '1', '11', '111'

# print(a)
# print(b)
# print(c)

# print(a.zfill(4))
# print(b.zfill(4))
# print(c.zfill(4))

# split() rsplit()
# myString = "I Love 2d and 3D graphics"
# myString2 = "I-Love-2d-and-3D-graphics"
# print(myString.split())
# print(myString2.split("-"))
# print(myString2.split("-", 2))
# print(myString2.rsplit("-", 2))
# print(type(myString.split()))

# center()
# x = "Ahmed mohamed"
# print(x.center(17))
# print(x.center(17, "#"))
# print(x.center(18, "#"))

# count()
# myString = "I Love python and SQL because SQL is easy"
# print(myString.count("SQL"))
# print(myString.count("SqL"))  # 0 because case sensitivity
# print(myString.count("SQL", 0, 25))  # search for SQL from index 0 to index 25


# swapcase()
# myString1 = "I Love PYTHON"
# myString2 = "i love Python"
# print(myString1.swapcase())
# print(myString2.swapcase())

# startswith()
# myString = "I Love python"
# print(myString.startswith("I"))
# print(myString.startswith("S"))
# print(myString.startswith("p", 7, 12))

# endswith()
# myString = "I Love python"
# print(myString.endswith("n"))
# print(myString.endswith("S"))
# print(myString.endswith("e", 2, 6))

# index()
# myString = "I Love python"
# print(myString.index("p"))
# print(myString.index("o"))
# print(myString.index("p", 0, 10))
# print(myString.index("p", 0, 5))  # Generates Error

# find(subString, start, end)
# myString = "I Love python"
# print(myString.find("p"))
# print(myString.find("o"))
# print(myString.find("p", 0, 10))
# print(myString.find("p", 0, 5))  # generates -1

# rjust()   ljust()
# x = "Ahmed"
# print(x.ljust(10))
# print(x.rjust(10))
# print(x.ljust(10, "#"))
# print(x.rjust(10, "#"))

# splitlines()
# e = """First Line
# Second Line
# Third Line"""
# a = "first \n second"
# print(e)
# print(a)
# print(e.splitlines())
# print(a.splitlines())
# print(type(a.splitlines()))

# expandtabs()
# g = "Hello\tworld\tI\tLove\tPython"
# print(g)
# print(g.expandtabs(2))
# print(g.expandtabs(3))

# istitle()
# myString = "I Love 2D And 3D Graphics"
# myString2 = "I Love 2d And 3D Graphics"
# print(myString.istitle())
# print(myString2.istitle())

# isspace()
# x = ""
# y = " "
# print(x.isspace())
# print(y.isspace())

# islower()
# isupper()
# x = "I Love Python"
# y = "i love python"
# z = "I LOVE PYTHON"
# print(x.isupper())
# print(y.isupper())
# print(z.isupper())
# print(x.islower())
# print(y.islower())
# print(z.islower())

# isidentifier()
# x = "Abdelrahman_Hossam"
# y = "Abdelrahman779"
# z = "Abdelrahman--hossam100"
# print(x.isidentifier())
# print(y.isidentifier())
# print(z.isidentifier())

# isalpha()
# isalnum()
# x = "ABCDefgs"
# y = "ABCDefgs700"
# z = "@#"
# print(x.isalpha())
# print(y.isalpha())
# print(x.isalnum())
# print(y.isalnum())
# print(z.isalnum())

# replace()
# a = "Hello one two three one one"
# print(a.replace("one", "1"))
# print(a.replace("one", "1", 1))
# print(a.replace("one", "1", 2))

# join()
# myList = ["Abdelrahman", "Hossam", "Sobhy"]
# print("_".join(myList))
# print(" ".join(myList))
# print(",".join(myList))
# print("@".join(myList))
# print(type(",".join(myList)))
