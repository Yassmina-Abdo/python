# ---------------------------------------------------------------------
# File Handling
# "a" Append  Open file for appending values, Create file if not exist
# "r" Read    [Default value] open file for read and give error if file is not exist
# "w" Write   open file for writing, create file if it is not exist
# "x" Create  create file, give error if file exists
# ---------------------------------------------------------------------

# Create a file called hi.txt
# file = open("Hi.txt", 'x')

file = open("Hi.txt", "r")  # == open("Hi.txt")
print(file)  # File Data object
print(file.name)
print(file.encoding)
print(file.mode)

# Takes number of bytes to be read, default value -1 to read all file data
# print(file.read())
# print(file.read(5))

# print(file.readline(10))
# print(file.readline())
# print(file.readline())
# print(file.readline())


# print(file.readlines())
# print(file.readlines(4))
# print(type(file.readlines()))


# for line in file:
#     if line.startswith("Sobhy"):
#         break
#     print(line)


# file.close()  # it is very important to close the file


# myFile = open("new.txt", "w")
# myFile.write("Hello From C\n")
# myFile.write("Hello world\n")

# myFile2 = open("Name.txt", "w")
# myFile2.write("Hello Abdelrahman Hosaam\n"*500)

# file = open("Hi.txt", "w")
# mylist = ["Abdelrahman\n", "Hossam\n", "Sobhy\n"]  # don't forget \n
# file.writelines(mylist)
# file.close()

# myFile = open("new.txt", "a")
# myFile.write("Hello From python\n")
# myFile.write("Hello world2")
# myFile.close()

# file = open("Hi.txt", "w")
# file.writelines("Hello world from python program")
# file.close()
# file = open("Hi.txt", "a")
# file.truncate(5)
# file.close()

# Works only with append mode
# file = open("Hi.txt", "a")
# print(file.tell())


# file = open("Hi.txt", "w")
# file.writelines("Hello From Python with Love")
# file.close()
# file = open("Hi.txt", "r")
# file.seek(2)
# print(file.read())


# import os
# if os.path.exists("Hi.txt"):
#     os.remove("Hi.txt")
# else:
#     print("File Not exist")
