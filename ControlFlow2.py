# ---------------------------------------------------------------------------
# -- Loop -- While, for
# ---------------------------------------------------------------------------

# while condition is true
# code will run

# a = 0
# while a < 15:
#     print(a)
#     a = a+1
# print("Finished")


# while False:
#     print("Will not print")


# myList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
# a = 0
# while a < len(myList):
#     print(myList[a])
#     a += 1
# print("==="*50)

# myList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
# a = 0
# while a < len(myList):
#     print(f"#{str(a+1).zfill(2)} {myList[a]}")
#     a += 1
# print("==="*50)

# =======================================================================

# myList = [2, 4, 7, 9, 3, 10, 5, 6, 8]
# for numbers in myList:
#     if numbers % 2 == 0:
#         print(f"Number {numbers} is Even Number")
#     else:
#         print(f"Number {numbers} is Odd Number")

# myName = "Abdelrahman"
# for letter in myName:
#     print(f"[ {letter} ]")

# range()
# myRange = range(1, 100)
# for number in myRange:
#     print(number)


# Dict()

mySkills = {
    "C": "90%",
    "Python": "70%",
    "Java": "80%",
    "Assembly": "750%",
    "C++": "50%"
}
# print(mySkills["Python"])
# print(mySkills.get("Java"))

# for skills in mySkills:
#     print(skills)

# for skills in mySkills:
#     print(f"My progress in [ {skills} ] ====> [ {mySkills[skills]} ]")


# peoples = ["Abdelrahman", "Ali", "Hamza"]
# skills = ["Python", "Java", "C"]
# for people in peoples:
#     print(people)
#     for skill in skills:
#         print(f"- {skill}")

# peoples = {
#     "Abdelrahman": {
#         "Python": "85%",
#         "Java": "70%",
#         "C": "95%"
#     },
#     "Ali": {
#         "Python": "70%",
#         "Java": "50%",
#         "C": "80%"
#     },
#     "Hamza": {
#         "Python": "95%",
#         "Java": "65%",
#         "C": "75%"
#     }
# }

# print(peoples["Abdelrahman"])
# print(peoples["Abdelrahman"]["C"])

# for name in peoples:
#     print(f"Skills and progress for {name}: ")
#     for skill in peoples[name]:
#         print(f"Your progress in {skill} is {peoples[name][skill]}")
#     print("="*40)


# mySkills = {
#     "C": "90%",
#     "Python": "70%",
#     "Java": "80%",
#     "Assembly": "750%",
#     "C++": "50%"
# }
# # print(mySkills.items())
# for skills, progress in mySkills.items():
#     print(f"{skills} ===> {progress}")


peoples = {
    "Abdelrahman": {
        "Python": "85%",
        "Java": "70%",
        "C": "95%"
    },
    "Ali": {
        "Python": "70%",
        "Java": "50%",
        "C": "80%"
    },
    "Hamza": {
        "Python": "95%",
        "Java": "65%",
        "C": "75%"
    }
}
# print(peoples.items())
for mainKey, mainValue in peoples.items():
    print(f"{mainKey} progress is")
    for childKey, childValue in mainValue.items():
        print(f"- {childKey} ==> {childValue}")
