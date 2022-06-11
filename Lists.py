# ----------------------------------------------------------------------
#  Lists
# [1] List Items are enclosed in square brackets
# [2] List is ordered, and we use index to access elements
# [3] List is Mutable ===> Add, Delete, Modify
# [4] List Items are not unique
# [5] List can have diffrent datatypes
# ----------------------------------------------------------------------
# This is my List
myList = ["one", "two", "one", 1, 7.54, True]

# How to print a List and its length
# ----------------------------------------------------------------------
print(myList)  # ['one', 'two', 'one', 1, 7.54, True]
print(len(myList))  # 6
print(type(myList))  # <class 'list'>

# Access List Elements 'Indexing'
# ----------------------------------------------------------------------
print(myList[1])  # two
print(myList[3])  # 1
print(myList[-1])  # True
print(myList[-4])  # one
print(type(myList[1]))  # <class 'str'>
print(type(myList[-1]))  # <class 'bool'>


# Indexing and slicing
# ----------------------------------------------------------------------
#["one", "two", "one", 1, 7.54, True]
# print(myList[1:4])  # ['two', 'one', 1]
# print(myList[:4])  # ['one', 'two', 'one', 1]
# print(myList[1:])  # ['two', 'one', 1, 7.54, True]
# print(myList[::1])  # ['one', 'two', 'one', 1, 7.54, True]
# print(myList[::2])  # ['one', 'one', 7.54]
# # print(myList[150])  # IndexError: list index out of range
# print(myList[-1:1])  # [] doesn't work in reverse
# print(myList[1:-1])  # ['two', 'one', 1, 7.54]
# print(myList[-4:-1])  # ['one', 1, 7.54]
# print(myList[::-1])  # [True, 7.54, 1, 'one', 'two', 'one']


# Edit list Items
print(myList)  # ['one', 'two', 'one', 1, 7.54, True]

# myList[2] = 3
# print(myList)  # ['one', 'two', 3, 1, 7.54, True]

# myList[-1] = False
# print(myList)  # ['one', 'two', 3, 1, 7.54, False]

# myList[0:3] = [0, 1, 2]
# print(myList)  # [0, 1, 2, 1, 7.54, False]

# myList[0:3] = ["z", "x"]
# print(myList)  # ["z", "x", 1, 7.54, False]

# myList[0:3] = []
# print(myList)  # [1, 7.54, False]

# myList[0:0] = ["A", "B", "C"]
# print(myList)  # ["A", "B", "C",1,  7.54, False]


# ----------------------------------------------------------------------
#  Lists Methodes
# ----------------------------------------------------------------------
myList = ['Abdelrahman', 'Hossam', 'Sobhy']
myOldList = ["Ahmed", "Mohamed", "Ali"]

# append()
# myList.append("Ibrahim")
# myList.append(25)
# myList.append(77.5)
# myList.append(True)
# myList.append(myOldList)

# ['Abdelrahman', 'Hossam', 'Sobhy', 'Ibrahim', 25, 77.5, True, ['Ahmed', 'Mohamed', 'Ali']]
# print(myList)
# print(myList[3])  # Ibrahim
# print(myList[6])  # True
# print(myList[7])  # ['Ahmed', 'Mohamed', 'Ali']
# what if i want to print an element from the second List for ex Ali
# print(myList[7][2])  # Ali
# print(myList[7][2][0])  # A

# extend()
# a = [1, 2, 3]
# b = ["A", "B", "C"]
# c = ["Hello", "World"]
# a.extend(b)
# print(a)  # [1, 2, 3, 'A', 'B', 'C']
# a.extend(c)
# print(a)  # [1, 2, 3, 'A', 'B', 'C', 'Hello', 'World']


# remove()
# myList = ['Abdelrahman', 'Hossam', 'Sobhy', 'Abdelrahman']
# myList.remove("Abdelrahman")
# print(myList)  # ['Hossam', 'Sobhy', 'Abdelrahman']
# myList.remove("Hi")  # ValueError: list.remove(x): x not in list

# sort()
# myList = [100, 70, 7, 55, -150, -2, 17, 29, -40]
# myList.sort()
# print(myList)  # [-150, -40, -2, 7, 17, 29, 55, 70, 100]
# myList.sort(reverse=True)
# print(myList)  # [100, 70, 55, 29, 17, 7, -2, -40, -150]

# myList = ["Ibrahim", "Abdelrahman", "Sobhy", "Hossam"]
# myList.sort()
# print(myList)  # ['Abdelrahman', 'Hossam', 'Ibrahim', 'Sobhy']

# myList = [1, 20, 3, 100, "A"]
# myList.sort() #TypeError: '<' not supported between instances of 'str' and 'int'


# reverse()
# myList = [1, 20, 3, 100, "A", 'Abdelrahman', 'Hossam', 'Ibrahim', 'Sobhy']
# myList.reverse()
# # ['Sobhy', 'Ibrahim', 'Hossam', 'Abdelrahman', 'A', 100, 3, 20, 1]
# print(myList)

# clear()
# myList = [1, 20, 3, 100, "A", 'Abdelrahman']
# myList.clear()
# print(myList)  # []

# copy() makes shallow copy this means it doesn't affect original list
# a = [1, 2, 3, 4]
# b = a.copy()
# a.append(5)
# print(a)  # [1, 2, 3, 4, 5]  main list
# print(b)  # [1, 2, 3, 4]   copied list

# count () just takes one argument
# a = [1, 2, 3, 4, 1, 5, 7, 1]
# print(a.count(1))  # 3
# print(a.count(0))  # 0

# index()
# myList = ['Abdelrahman', 'Hossam', 'Ibrahim', 'Sobhy', 'Hossam', 'Hossam']
# print(myList.index('Hossam'))  # index number 1
# print(myList.index('Hossam', 3, len(myList)))  # index number 4
# print(myList.index('Ahmed'))  # ValueError: 'Ahmed' is not in list

# insert()
# a = [1, 2, 3, 4]
# a.insert(0, "Abdelrahman")
# print(a)  # ['Abdelrahman', 1, 2, 3, 4]
# a.insert(-1, "Hossam")
# print(a)  # ['Abdelrahman', 1, 2, 3, 'Hossam', 4]
# a.insert(5, "9")
# print(a)

# pop()
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(a.pop(2))  # 3
print(a)  # [1, 2, 4, 5, 6, 7, 8]
