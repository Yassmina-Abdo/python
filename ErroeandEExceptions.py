# ---------------------------------------------------------------------
# Error and Exception Raising
# [1] Exception is a run time error reproting mechanism
# [2] Exception gives you the message to understand the error
# [3] Traceback gives you the line to look for in the code
# [4] Exceptions have types [Syntax Error, Index Error, keyerror, Etc...]
# [5] Exceptions List http://docs.python.org/3/library/exceptions.html
# [6] raise keyword is used to raise your own Exception
# ---------------------------------------------------------------------

# x = -10

# if x < 0:
#     print(f"The number you entered is {x} and it is less than Zero")
# else:
#     print("The number is ok")
# print("Finished")


# x = -10

# if x < 0:
#     raise Exception(f"The number you entered is {x} and it is less than Zero")
#     print("This will not print")
# else:
#     print("The number is ok")
# print("Finished")


# a = "Abdelrahman"
# # if a != int:
# #     print("Only Number allowed")
# # print("Finished")

# if a != int:
#     raise ValueError("Only Number allowed")
# print("Finished")

# ---------------------------------------------------------------------
# Error and Exception Handling
# Try | Except | Else | Finally
# Try    ===> Test the code Error
# Except ===> Handle the Errors
# Else   ===> If no error
# Finally===> Runs the program
# ---------------------------------------------------------------------

# number = int(input("Enter your age: "))
# print(number)
# print(type(number))


# try:  # Try the code and Test Errors
#     number = int(input("Enter your age: "))
# except:  # Handle the Errors if it is Found
#     print("This is not an Int")
# print("Hello")

# try:  # Try the code and Test Errors
#     number = int(input("Enter your age: "))
#     print("This is Int from Try")
# except:  # Handle the Errors if it is Found
#     print("This is not an Int")
# else:  # If there is no Error (you can ignore else and continue in try)
#     print("This is Int from Else")

# try:  # Try the code and Test Errors
#     number = int(input("Enter your age: "))
#     print("This is Int from Try")
# except:  # Handle the Errors if it is Found
#     print("This is not an Int")
# else:  # If there is no Error (you can ignore else and continue in try)
#     print("This is Int from Else")
# finally:  # Runs the program
#     print("Hi")

# This is a problem
# try:
# a = 10/0
# print(x)
# except:
#     print("can't divide on 0")

# try:
# a = 10/0
# print(x)
# print(int("Hello"))  # Value Error
# except ZeroDivisionError:
#     print("can't divide on 0")
# except NameError:
#     print("Identifier not Found")
# except:
#     print("Error Happens")


# NumberOfTries = 5
# myFile = None
# while NumberOfTries > 0:
#     try:
#         print("Enter The File Name with its full path")
#         print(f"You have {NumberOfTries} Tries Left")
#         print("Example:- /Users/abdelrahmanhossam/Documents/pythonCourse/File.txt")
#         path = input("Enter path:-  ").strip()
#         myFile = open(path, 'r')
#         print(myFile.read())
#         break
#     except FileNotFoundError:
#         print("File Not Found, Try Again")
#         NumberOfTries -= 1
#     except:
#         print("Sorry, There is an Error")
#     finally:
#         if myFile is not None:
#             myFile.close()
#             print("File Closed")
# else:
#     print("All Tries are done")


# try:
#     x = int(input("Please Enter a number: "))
#     if x < 0:
#         raise Exception("Not Allowed")
#     else:
#         print("That is not an error")
# except ValueError:
#     print("That is not an int")
# except:
#     print("That is an error")
