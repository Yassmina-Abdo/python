# ----------------------------------------------------------------------
#  Set
# [1] Set Items are enclosed in curly braces
# [2] Set isn't ordered, and isn't indexed
# [3] set indexing and slicing cannot be done
# [4] Set has only Immutable datatypes (Numbers, String, Tuples) List and Dict are not
# [5] Items are unique
# ----------------------------------------------------------------------

# not ordered and not indexed
# mySetOne = {"Abdelrahman", "Hossam", "100"}
# print(mySetOne)
# print(mySetOne[0])  # TypeError: 'set' object is not subscriptable

# Slicing cannot be done
# print(mySetOne[0:3])  # TypeError: 'set' object is not subscriptable


# only Immutable datatypes
# mySetOne = {"Abdelrahman", 7.7, "100", True, [1, 2, 3]}
# print(mySetOne)  # TypeError: unhashable type: 'list

# mySetOne = {"Abdelrahman", 7.7, "100", True, (1, 2, 3)}
# print(mySetOne)

# Items are unique
# mySetOne = {"Abdelrahman", 7.7, "100", True, "Abdelrahman", 100, 7.7}
# print(mySetOne)  # {True, 'Abdelrahman', '100', 7.7}


# clear()
# mySetOne = {"Abdelrahman", 7.7, "100", True}
# mySetOne.clear()
# print(mySetOne)  # set()

# union()
# a = {"One", "Two", "Three"}
# b = {1, 2, 3}
# c = {"i", "ii", "iii"}
# print(a | b)  # {1, 2, 3, 'One', 'Three', 'Two'}
# print(a.union(b))  # {1, 2, 3, 'One', 'Three', 'Two'}
# print(a | b | c)  # {1, 2, 3, 'Three', 'Two', 'i', 'ii', 'One', 'iii'}
# print(a.union(b, c))  # {1, 2, 3, 'Three', 'Two', 'i', 'ii', 'One', 'iii'}

# add()
# b = {1, 2, 3, 4}
# b.add(5)
# b.add(5, 6) #TypeError: set.add() takes exactly one argument (2 given)
# print(b)  # {1, 2, 3, 4, 5}


# copy()
# a = {1, 2, 3, 4}
# b = a.copy()
# print(a)  # {1, 2, 3, 4}
# print(b)  # {1, 2, 3, 4}
# b.add(5)
# print(a)  # {1, 2, 3, 4}
# print(b)  # {1, 2, 3, 4, 5}


# remove ()
# a = {1, 2, 3, 4, 5}
# a.remove(3)
# print(a)  # {1, 2, 4, 5}
# a.remove(7)  # KeyError: 7

# discard ()
# a = {1, 2, 3, 4, 5}
# a.discard(3)
# print(a)  # {1, 2, 4, 5}
# a.discard(7)
# print(a)  # {1, 2, 4, 5}


# pop()
# a = {"A", 1, 2, 3, 4, 5, True}
# print(a.pop())
# print(a)


# update ()
# j = {1, 2, 3}
# k = {1, "A", "H", 7}
# j.update(k)
# print(j)  # {1, 2, 3, 'A', 'H', 7}
# j.update(["Python", "Java"])
# print(j)  # {1, 2, 3, 'A', 'H', 'Java', 7, 'Python'}


# difference()
# a = {1, 2, 3, 4}
# b = {1, 2, "A", "D"}
# print(a.difference(b))  # {3, 4}
# print(a)  # {1, 2, 3, 4}
# print(b.difference(a))  # {'A', 'D'}
# print(b)  # {1, 2, "A", "D"}
# print("-"*50)
# print(a-b)  # {3, 4}
# print(b-a)  # {'A', 'D'}


# difference_update()
# a = {1, 2, 3, 4}
# b = {1, 2, "A", "D"}
# print(a)  # {1, 2, 3, 4}
# a.difference_update(b)
# print(a)  # {3, 4}

# intersection()
# a = {1, 2, 3, 4}
# b = {1, 2, "A", "D"}
# print(a)  # {1, 2, 3, 4}
# print(a.intersection(b))  # {1, 2}
# print(a)  # {1, 2, 3, 4}
# print(a & b)  # {1, 2}

# intersection_update()
# a = {1, 2, 3, 4}
# b = {1, 2, "A", "D"}
# print(a)  # {1, 2, 3, 4}
# a.intersection_update(b)
# print(a)  # {1, 2}

# symmetric_difference()
# a = {1, 2, 3, 4}
# b = {1, 2, "A", "D"}
# print(a)  # {1, 2, 3, 4}
# print(a.symmetric_difference(b))  # {3, 4, 'A', 'D'}
# print(a)  # {1, 2, 3, 4}
# print(a ^ b)  # {3, 4, 'A', 'D'}

# symmetric_difference_update()
# a = {1, 2, 3, 4}
# b = {1, 2, "A", "D"}
# print(a)  # {1, 2, 3, 4}
# a.symmetric_difference_update(b)
# print(a)  # {'A', 3, 4, 'D'}


# issuperset()
# a = {1, 2, 3, 4, 5, 6, 7, "A", "B", "C"}
# b = {1, 2, "A", "D"}
# c = {7, 5, "A", "C"}
# print(a.issuperset(b))  # False
# print(a.issuperset(c))  # True

# issubset()
# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# c = {7, 5, "A", "C", 1, 2, 3, 4}
# print(a.issubset(b))  # False
# print(a.issubset(c))  # True


# isdisjoint()
# g = {1, 2, 3}
# h = {1, 2, 6, 7}
# i = {10, 11, 12}
# print(g.isdisjoint(h))  # False
# print(g.isdisjoint(i))  # True
