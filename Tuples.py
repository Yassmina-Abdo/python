# ----------------------------------------------------------------------
#  Tuples
# [1] Tuple Items are enclosed in parentheses
# [2] you can remove the parentheses if you want
# [3] Tuple is ordered, and we use index to access it
# [4] Tuple is Immutable ===> you can't (Add, Delete)
# [5] Tuple Items are not unique
# [6] Tuple can have diffrent datatypes
# [7] Operators used in String and List can be used in tuples
# ----------------------------------------------------------------------

# This is my Tuple
myTupleOne = ("one", "two")
myTupleTwo = "one", "two"

# print tuple and its type and length
# print(myTupleOne)  # ("one", "two")
# print(myTupleTwo)  # ("one", "two")
# print(type(myTupleOne))  # Tuple
# print(type(myTupleTwo))  # Tuple
# print(len(myTupleOne))  # 2
# print(len(myTupleTwo))  # 2

# Tuple Indexing and slicing
# myTupleOne = (1, 2, 3, 4, 5, 6, 7)
# print(myTupleOne[0])  # 1
# print(myTupleOne[3])  # 4
# print(myTupleOne[-1])  # 7
# print(myTupleOne[-3])  # 5
# print(myTupleOne[0:3])  # 1, 2, 3
# print(myTupleOne[0:])  # (1, 2, 3, 4, 5, 6, 7)
# print(myTupleOne[:5])  # (1, 2, 3, 4, 5)
# print(myTupleOne[-1:1])  # () doesn't work in reverse
# print(myTupleOne[1:-1])  # (2, 3, 4, 5, 6)
# print(myTupleOne[-4:-1])  # (4, 5, 6)
# print(myTupleOne[100])  # IndexError: tuple index out of range

# myTupleOne = (1, 2, 3, ["Abdelrahman", "Hossam"], 5, 6, 7)
# print(myTupleOne[3][0])  # Abdelrahman
# myTupleOne[3][0] = 9
# print(myTupleOne[3][0])  # 9

# Tuple Assign Values
# myTupleOne = (1, 2, 3, 4, 5, 6, 7)
# # TypeError: 'tuple' object does not support item assignment
# myTupleOne[2] = "Three"


# Tuple items
# myTupleOne = ("Abdelrahman", True, 3, "Abdelrahman", 5, False, 7)
# print(myTupleOne[0])  # Abdelrahman
# print(myTupleOne[3])  # Abdelrahman
# print(myTupleOne[-1])  # 7
# print(myTupleOne[-3])  # 5


# Tuple with one element
# myTupleOne = ("one")
# myTupleTwo = "one"
# print(myTupleOne)
# print(myTupleTwo)
# print(type(myTupleOne))  # String
# print(type(myTupleTwo))  # String
# print(len(myTupleOne))  # 3 (length of string)
# print(len(myTupleTwo))  # 3 (length of string)
# To solve this problem and make it a Tuple
# myTupleOne = ("one",)
# myTupleTwo = "one",
# print(myTupleOne)
# print(myTupleTwo)
# print(type(myTupleOne))  # Tuple
# print(type(myTupleTwo))  # Tuple
# print(len(myTupleOne))  # 1
# print(len(myTupleTwo))  # 1

# concatenation
# a = (1, 2, 3, 4, 5)
# b = (6, 7, 8)
# c = a+b
# d = a + ("A", "B", "C") + b
# print(c)  # (1, 2, 3, 4, 5, 6, 7, 8)
# print(d)  # (1, 2, 3, 4, 5, 'A', 'B', 'C', 6, 7, 8)


# Tuple, List, String Repeat (*)
# a = "Abdelrahman "
# b = [1, 2, 3, 4, 5, 6, 7]
# c = ("Hossam ",)
# print(a * 5)
# print(b * 5)
# print(c * 5)
# print("==" * 50)

# count()
a = (1, 2, 3, 2, 5, 1, 7)
# print(a.count(2))  # 2
# TypeError: tuple.count() takes exactly one argument (3 given)
# print(a.count(2, 0, 3))

# index()
# a = (1, 2, 3, 2, 5, 1, 7)
# print(a.index(3))  # 2
# # 1 (search from index 0 to 5, note that index number 5 is not included)
# print(a.index(5, 0, 5))

# Tuple Destruct
# w = "A", "B", "C"
# x, y, z = "D", "Z", "X"
# print(x, y, z)  # D Z X
# a, b, c = w
# print(a, b, c)  # A B C

w = "A", "B", 5, "C"
# a, b, c = w  # ValueError: too many values to unpack (expected 3)
# How to Solve ?
# a, b, _, c = w
# print(a, b, c)  # A B C
# print(_)
