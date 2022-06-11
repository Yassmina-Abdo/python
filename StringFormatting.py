# print using format specifier
# for string  %s
# for float   %f
# for  Integer %d

name = "Abdelrahman"
age = 25
rank = 10.77

# print("My Name is: " + name)
# print("My Name is: " + name + " and my age is: " + age)  # error

# print("My Name is: %s " % (name))
# print("My Name is: %s  and my age is: %d" % (name, age))
# print("My Name is: %s  and my age is: %d and my rank is: %d" % (name, age, rank))
# print("My Name is: %s  and my age is: %d and my rank is: %f" % (name, age, rank))

# control floating point
# print("My Name is: %s  and my age is: %d and my rank is: %.0f" % (name, age, rank))

# Truncate String
# msg = "Hello People of ITI"
# print("msg is %s" % (msg))
# print("msg is %.5s" % (msg))

# =================================================================
# New way for Format
# print("My name is {} and my age is {}".format(name, age))

# print("My name is {:s} and my age is {:d} and my rank is {:f}".format(
#     name, age, rank))

# print("My name is {:s} and my age is {:d} and my rank is {:.2f}".format(
#     name, age, rank))

# Money Format
# Money = 779685685973564
# print("My Money = {:d}".format(Money))
# print("My Money = {:_d}".format(Money))
# print("My Money = {:,d}".format(Money))
# print("My Money = {:,}".format(Money))
# print("My Money = {:@d}".format(Money))  # ValueError: Invalid format specifier

# =================================================================
# Rearrange Items
# a, b, c = "Zero", "one", "Two"
# print("Hello {} {} {}".format(a, b, c))
# print("Hello {1} {2} {0}".format(a, b, c))

# x, y, z, w = 10, 20, 30, "Hello People"
# print("Hello {1:d} {2:.2f} {0:f} {3:.5s}".format(x, y, z, w))

# =================================================================
# Format in version 3.6+
# print(f"My name is {name} and my age is {age} and my rank is {rank}")
# print(f"My name is {name} and my age is {age} and my rank is {rank:.4f}")
