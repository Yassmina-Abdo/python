# ------------------------------------------
# Class
# [01] Class is the blueprint or constructor of the object
# [02] Class instantiate means create Instance of the class
# [03] Instance => object created from the call and has its methods and attributes
# [04] Class defined with keyword class
# [05] Class name is written with pascal case [UpperCamalCase] style
# [06] Class may contain methods and attributes
# [07] when creating object python looks for __init__ Method
# [08] __init__ Method called everytime you create object from the class
# [09] __init__ Method is intializing the data for the object
# [10] Any method with two _ in the start or the end called Dunder or Magic method
# [11] Self refer to the current instance created from the class and must be first parameter
# [12] Self can be named anything
# [13] In python you don't need to use new() keyword to create object


# Syntax
# class member:

#     def __init__(self):
#         print("A new member has been added")


# member()
# member()
# member()
# print(type("Abdelrahman"))
# print(dir(str))
# print(dir(member))
# member_one = member()
# member_two = member()
# member_three = member()
# print(member_one.__class__)
# print(type(member_one))


# ------------------------------------------
# Instance attributes and methods
# [01] Self points to Instance created from a class
# [02] Instance attributes defined Inside the constructor


# class Member:
#     def __init__(self):
#         self.name = "Abdelrahman"


# member_one = Member()
# member_two = Member()
# member_three = Member()

# print(member_one.name)
# print(member_two.name)
# print(member_three.name)


# class Member:

#     def __init__(self, firstName):
#         self.name = firstName


# member_one = Member("Abdelrahman")
# member_two = Member("Hossam")
# member_three = Member()  # Error

# print(member_one.name)
# print(member_two.name)
# print(id(member_one))
# print(id(member_two))
# print("*"*50)
# print(id((member_one.name)))
# print(id((member_two.name)))
# print(member_three.name)


# class Member:
#     def __init__(self, fName, mName, lName):
#         self.name1 = fName
#         self.name2 = mName
#         self.name3 = lName

#     def fullName(self):
#         return f"{self.name1} {self.name2} {self.name3}"


# member_one = Member("Abdelrahman", "Hossam", "Sobhy")
# member_two = Member("Hossam", "Sobhy", "Ibrahim")

# print(member_one.fullName())


# class Member:
#     def __init__(self, fName, mName, lName):
#         self.name1 = fName
#         self.name2 = mName
#         self.name3 = lName

#     def fullName(self):
#         return f"{self.name1} {self.name2} {self.name3}"

#     def helloMsg(self):
#         return f"Hello Mr {self.name1}"


# member_one = Member("Abdelrahman", "Hossam", "Sobhy")
# member_two = Member("Hossam", "Sobhy", "Ibrahim")
# member_three = Member("Doaa", "Ahmed", "Mohamed")

# print(member_one.fullName())
# print(member_two.helloMsg())
# print(member_three.helloMsg())  # ????!


# class Member:
#     numberOfObjects = 0

#     def __init__(self, fName, mName, lName, gender):
#         self.name1 = fName
#         self.name2 = mName
#         self.name3 = lName
#         self.gender = gender
#         Member.numberOfObjects += 1

#     def fullName(self):
#         return f"{self.name1} {self.name2} {self.name3}"

#     def helloMsg(self):
#         if self.gender is "Male":
#             return f"Hello Mr {self.name1}"
#         elif self.gender is "Female":
#             return f"Hello Miss {self.name1}"
#         else:
#             return f"Hello, {self.name1}"

#     def getFullInfo(self):
#         return f"{self.helloMsg()}, your full name is {self.fullName()}"


# print(Member.numberOfObjects)
# member_one = Member("Abdelrahman", "Hossam", "Sobhy", "Male")
# member_two = Member("Hossam", "Sobhy", "Ibrahim", "Male")
# member_three = Member("Doaa", "Ahmed", "Mohamed", "Female")
# print(Member.numberOfObjects)
# print(member_one.fullName())
# print(member_two.helloMsg())
# print(member_three.helloMsg())
# print(member_one.getFullInfo())

# print(dir(Member))
# print(member_one.__class__)
# print(type(member_one))
# --------------------------------------------------------------
# class Member:
#     numberOfObjects = 0

#     @classmethod
#     def getUsersNumber(cls):
#         return f"{cls.numberOfObjects}"

#     @classmethod
#     def showUserCount(cls):
#         print(f"Number of users in the system = {cls.numberOfObjects}")

#     @staticmethod
#     def say_Hello():
#         print("Hello From Static Method")

#     def __init__(self, fName, mName, lName, gender):
#         self.name1 = fName
#         self.name2 = mName
#         self.name3 = lName
#         self.gender = gender
#         Member.numberOfObjects += 1

#     def fullName(self):
#         return f"{self.name1} {self.name2} {self.name3}"

#     def helloMsg(self):
#         if self.gender is "Male":
#             return f"Hello Mr {self.name1}"
#         elif self.gender is "Female":
#             return f"Hello Miss {self.name1}"
#         else:
#             return f"Hello, {self.name1}"

#     def getFullInfo(self):
#         return f"{self.helloMsg()}, your full name is {self.fullName()}"

#     def deleteUser(self):
#         Member.numberOfObjects -= 1
#         print(f"\"{self.fullName()}\" has been deleted")


# print(f"Number of users in the system = {Member.getUsersNumber()}")
# member_one = Member("Abdelrahman", "Hossam", "Sobhy", "Male")
# member_two = Member("Hossam", "Sobhy", "Ibrahim", "Male")
# member_three = Member("Doaa", "Ahmed", "Mohamed", "Female")
# print(member_one.fullName())
# print(Member.helloMsg(member_two))  # Happens in background
# print(member_three.helloMsg())
# print(member_one.getFullInfo())
# Member.showUserCount()
# member_two.deleteUser()
# Member.showUserCount()
# Member.say_Hello()

# ----------------------------------------------------------------------

# class skill:
#     def __init__(self):
#         self.skills = ["C", "Python", "Java"]


# Myskills = skill()
# print(Myskills)
# print(Myskills.__class__)


# myString = "Abdelrahman"
# print(type(myString))
# print(myString.__class__)
# print(dir(str))
# print(str.upper(myString))
# print(myString.upper())

# myString = 12
# print(type(myString))
# print(myString.__class__)
# print(dir(int))


# class skill:
#     def __init__(self):
#         self.skills = ["C", "Python", "Java"]


# Myskills = skill()
# print(Myskills.__str__)  # ???!
# print(Myskills.__class__)


# class skill:
#     def __init__(self):
#         self.skills = ["C", "Python", "Java"]

#     def __str__(self):
#         return f"This is my Skills"

#     def __len__(self):
#         return len(self.skills)


# Myskills = skill()
# print(Myskills)
# print(Myskills.__str__())
# print(Myskills.__len__())
# print(len(Myskills))

# Myskills.skills.append("Assembly")
# Myskills.skills.append("PS")
# print(len(Myskills))

# --------------------------------------------------------
# class PowerSolution:
#     def pow(self, x, n):
#         if x == 0 or x == 1 or n == 1:
#             return x
#         if x == -1:
#             if n % 2 == 0:
#                 return 1
#             else:
#                 return -1
#         if n == 0:
#             return 1
#         if n < 0:
#             return 1/self.pow(x, -n)
#         val = self.pow(x, n//2)
#         if n % 2 == 0:
#             return val * val
#         return val * val * x

# print(PowerSolution().pow(2, 4))

# --------------------------------------------------------
# class Food:
#     def __init__(self):
#         print("This is super class")


# class Apple:
#     def __init__(self):
#         print("This is derived class")


# foodOne = Food()
# foodTwo = Apple()


# class Food:
#     def __init__(self):
#         print("This is super class")

#     def eat(self):
#         print("Eat method from base class")


# class Apple(Food):
#     def __init__(self):
#         print("This is derived class")


# foodOne = Food()
# foodTwo = Apple()
# foodTwo.eat()


# class Food:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is super class")

#     def eat(self):
#         print("Eat method from base class")


# class Apple(Food):
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is derived class")


# foodOne = Food("pizza")
# foodTwo = Apple("pizza")
# foodTwo.eat()


# class Food:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is super class")

#     def eat(self):
#         print("Eat method from base class")


# class Apple(Food):
#     def __init__(self, name):
#         # Food.__init__(self, name)  # Create instance from base class
#         super().__init__(name)
#         print(f"{self.name} is derived class")


# foodOne = Food("pizza")
# foodTwo = Apple("pizza")
# foodTwo.eat()


# class Food:
#     numberofFood = 20

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} is super class and its price = {self.price}")

#     def eat(self):
#         print("Eat method from base class")


# class Apple(Food):
#     def __init__(self, name, price, amount):
#         # Food.__init__(self,name) # Create instance from base class
#         super().__init__(name, price)
#         self.amount = amount
#         print(
#             f"{self.name} is derived class and its price = {self.price} and amount = {self.amount}")


# foodOne = Food("pizza", 50)
# foodTwo = Apple("pizza", 70, 150)
# foodTwo.eat()
# print(foodTwo.numberofFood)


# ---------------------------------------------------------------------------------
# class Food:

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} is super class and its price = {self.price}")

#     def eat(self):
#         print("Eat method from base class")


# class Apple(Food):
#     def __init__(self, name, price, amount):
#         # Food.__init__(self,name) # Create instance from base class
#         super().__init__(name, price)
#         self.amount = amount
#         print(
#             f"{self.name} is derived class and its price = {self.price} and amount = {self.amount}")

#     def eat(self):
#         print("Eat method from derived class")


# # foodOne = Food("pizza")
# foodTwo = Apple("pizza", 50, 150)
# foodTwo.eat()
# ---------------------------------------------------------------------------------

# class BaseOne:
#     def __init__(self):
#         print("Base One")


# class BaseTwo:
#     def __init__(self):
#         print("Base Two")


# class DerivedClass (BaseOne, BaseTwo):
#     pass


# myVar = DerivedClass()
# print(DerivedClass.mro())  # method resolution order

# ---------------------------------------------------------------------------------

# class BaseOne:
#     def __init__(self):
#         print("Base One")

#     def func1(self):
#         print("Function 1")


# class BaseTwo:
#     def __init__(self):
#         print("Base Two")

#     def func2(self):
#         print("Function 2")


# class DerivedClass (BaseOne, BaseTwo):
#     pass


# myVar = DerivedClass()
# print(myVar.func1)
# print(myVar.func2)

# myVar.func1()
# myVar.func2()

# ---------------------------------------------------------------------------------
# polymorphism

# n1 = 10
# n2 = 20
# print(n1 + n2)

# s1 = "Love"
# s2 = "Python"
# print(s1 + " " + s2)

# print(len([1, 2, 3, 4, 5, 6, 7]))
# print(len("Abdelrahman"))
# print(len({"Key_one": 1, "Key_Two": 2}))


# class A:
#     def doSomething(self):
#         print("From Class A")


# class B(A):
#     pass


# my_Instance = B()
# my_Instance.doSomething()

# -------------------------------

# class A:
#     def doSomething(self):
#         print("From Class A")


# class B(A):
#     def doSomething(self):
#         print("From Class B")


# my_Instance = B()
# my_Instance.doSomething()
# --------------------------------------
# class A:
#     def doSomething(self):
#         print("From Class A")
#         raise NotImplementedError("Derived class must implement this method")


# class B(A):
#     def doSomething(self):
#         print("From Class B")


# class C(A):
#     pass


# my_Instance = C()
# my_Instance.doSomething()


# -------------------------------------------------------

# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")

#     def language(self):
#         print("Hindi is the most widely spoken language of India.")

#     def type(self):
#         print("India is a developing country.")


# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")

#     def language(self):
#         print("English is the primary language of USA.")

#     def type(self):
#         print("USA is a developed country.")


# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()
# --------------------------------------------------------------------

# Encapsulation
# Restrict Access to data stored in attributes and methods
# Public
# Every Attribute we used so far is public
# Attributes and Methodes can be modified and run from everywhere inside or outsode the class
# protected
# Attributes and Methods can be Accessed from within the class or sub classes
# Attributes and methods prefixed with one underscore _
# Private
# Attributes and Methods can be Accessed from within the class or object only
# Attributes cannot be modified from outside the class
# Attributes and methods prefixed with Two underscore __
# ----------------------------------------------------------------------
# Attributes - Variables - Properties
# ----------------------------------------------------------------------

# class people:
#     def __init__(self, name):
#         self.name = name
#         print(f"Your name is {self.name}")


# one = people("Ahmed")
# one.name = "Mohamed"
# print(one.name)

# --------------------------------------------------
# class people:
#     def __init__(self, name):
#         self._name = name  # protected
#         print(f"Your name is {self._name}")


# one = people("Ahmed")
# one._name = "Mohamed"
# print(one._name)

# --------------------------------------------------
# class people:
#     def __init__(self, name):
#         self.__name = name


# one = people("Ahmed")
# print(one.__name)

# --------------------------------------------------
# class people:
#     def __init__(self, name):
#         self.__name = name

#     def sayHello(self):
#         return f"Hello {self.__name}"


# one = people("Ahmed")
# print(one.sayHello())
# --------------------------------------------------
# class people:
#     def __init__(self, name):
#         self.__name = name

#     def sayHello(self):
#         return f"Hello {self.__name}"


# one = people("Ahmed")
# print(one.sayHello())
# print(one._people__name)
# one.__name = "Mohamed"  # created new var
# print(one.__name)  # print the new var
# one._people__name = "Ali"
# print(one._people__name)
# print(one.sayHello())
# --------------------------------------------------

# Getters and Setters

# class people:
#     def __init__(self, name):
#         self.__name = name

#     def sayHello(self):
#         return f"Hello {self.__name}"

#     def GetName(self):
#         return self.__name

#     def SetName(self, newName):
#         self.__name = newName

# --------------------------------------------------
# class programming:
#     def has_oop(self):
#         return "Yes"


# class Python(programming):
#     def has_oop(self):
#         return "Yes"


# class Pascal(programming):
#     def has_oop(self):
#         return "No"


# one = programming()
# print(one.has_oop())  # ??!!!

# ----------------------------------------------------

# from abc import ABCMeta, abstractmethod


# class programming(metaclass=ABCMeta):
#     @abstractmethod
#     def has_oop(self):
#         pass


# class Python(programming):
#     def has_oop(self):
#         return "Yes"


# class Pascal(programming):
#     def has_oop(self):
#         return "No"


# one = programming()
# print(one.has_oop())  # Error

# one = Python()
# print(one.has_oop())
