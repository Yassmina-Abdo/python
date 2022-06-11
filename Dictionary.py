# --------------------------------------
# Dictionary
# [1] Dict Items are enclosed in curly braces
# [2] Dict Items are containing Key : Value
# [3] Dict key needs to be immutable => (Number, String, Tuple) List is not allowed
# [4] Dict value can be any type od data
# [5] Dict key must be unique
# [6] Dict is not ordered, you can access its elements with key


# myDict = {
#     "Name": "Abdelrahman",
#     "Age": 25,
#     "Country": "Egypt",
#     "Skills": ["C", "Java", "Python"],
#     "Rating": 10.5
# }
# print(myDict)

# myDict = {
#     "Name": "Abdelrahman",
#     "Age": 25,
#     "Country": "Egypt",
#     "Skills": ["C", "Java", "Python"],
#     "Rating": 10.5,
#     "Name": "Ahmed"
# }
# print(myDict)
# print(myDict["Country"])  # Egypt
# print(myDict.get("Country"))  # Egypt
# # dict_keys(['Name', 'Age', 'Country', 'Skills', 'Rating'])
# print(myDict.keys())
# # dict_values(['Ahmed', 25, 'Egypt', ['C', 'Java', 'Python'], 10.5])
# print(myDict.values())

# Two Dimensional Dict

# languages = {
#     "One": {
#         "name": "C",
#         "Progress": "80%"
#     },
#     "Two": {
#         "name": "Python",
#         "Progress": "70%"
#     },
#     "Three": {
#         "name": "Java",
#         "Progress": "90%"
#     }
# }

# print(languages)
# print(languages["One"])
# print(languages["Three"]["Progress"])
# print(len(languages))
# print(len(languages["Two"]))


# one = {
#     "name": "C",
#     "Progress": "80%"
# }
# two = {
#     "name": "Python",
#     "Progress": "70%"
# }
# three = {
#     "name": "Java",
#     "Progress": "90%"
# }
# allLanguages = {
#     "One": one,
#     "Two": two,
#     "Three": three
# }
# print(allLanguages)
# print(allLanguages["One"])
# print(allLanguages["Three"]["Progress"])
# print(len(allLanguages))
# print(len(allLanguages["Two"]))


# clear()
# myDict = {"Name": "Abdelrahman"}
# print(myDict)
# myDict.clear()
# print(myDict)


# update()
# myDict = {"Name": "Abdelrahman"}
# print(myDict)
# myDict["Age"] = 25
# print(myDict)
# myDict.update({"Country": "Egypt"})
# print(myDict)
# myDict.update({"Skill1": "Python", "Skill2": "C"})
# print(myDict)

# copy()
# myDict = {"Name": "Abdelrahman"}
# Dict2 = myDict.copy()
# print(myDict)
# print(Dict2)
# Dict2["Age"] = 25
# print(myDict)
# print(Dict2)


# setdefault()
# myDict = {"Name": "Abdelrahman"}
# print(myDict)
# print(myDict.setdefault("Name", "Ali"))
# print(myDict)
# print(myDict.setdefault("Age", 25))
# print(myDict)
# print(myDict.setdefault("Skill"))
# print(myDict)

# popitem() (before version 3.7 of python it returns randome item)
# myDict = {"Name": "Abdelrahman"}
# myDict["Age"] = 25
# print(myDict)
# print(myDict.popitem())
# print(myDict)

# items()
# myDict = {"Name": "Abdelrahman", "Skills": "Python"}
# print(myDict)
# Dict2 = myDict.items()
# myDict["Age"] = 25
# print(Dict2)

# fromkeys()
a = ("One", "Two", "Three")
b = "z"
c = [1, 2, 3]
d = (1, 2, 3)
myDict = dict.fromkeys(a, b)
print(myDict)
myDict2 = dict.fromkeys(a, c)
print(myDict2)
myDict3 = dict.fromkeys(a, d)
print(myDict3)
