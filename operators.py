# ---------------------------------------------------------------------------
# Operators
# ---------------------------------------------------------------------------

# Remember casting
# value = input("Please enter a number: ")
# value2 = input("Please enter another number: ")
# value3 = int(value) + int(value2)
# print(value3)
# ---------------------------------------------------------------------------

# Arithmetic Operators
# +	 Addition: adds two operands	x + y
# –	 Subtraction: subtracts two operands	x – y
# *	 Multiplication: multiplies two operands	x * y
# /	 Division (float): divides the first operand by the second	x / y
# // Division (floor): divides the first operand by the second	x // y
# %	 Modulus: returns the remainder when the first operand is divided by the second	x % y
# ** Power: Returns first raised to power second	x ** y

# Examples of Arithmetic Operator
# a = 9
# b = 4
# add = a + b  # Addition of numbers
# sub = a - b  # Subtraction of numbers
# mul = a * b  # Multiplication of numbers
# div1 = a / b  # Division(float) of numbers
# div2 = a // b  # Division(floor) of numbers
# mod = a % b  # Modulo of both numbers
# p = 2 ** 3  # Power

# # print results
# print(f"Addition of numbers = {add}")
# print(f"Subtraction of numbers = {sub}")
# print(f"Multiplication of numbers = {mul}")
# print(f"Division(float) of numbers = {div1}")
# print(f"Division(floor) of numbers = {div2}")
# print(f"Modulo of both numbers = {mod}")
# print(f"Power (2^3) = {p}")
# ---------------------------------------------------------------------------

# Comparison Operators or Relational Operators
# >	Greater than: True if the left operand is greater than the right	x > y
# <	Less than: True if the left operand is less than the right	x < y
# ==	Equal to: True if both operands are equal	x == y
# !=	Not equal to – True if operands are not equal	x != y
# >=	Greater than or equal to True if the left operand is greater than or equal to the right	x >= y
# <=	Less than or equal to True if the left operand is less than or equal to the right	x <= y

# Examples of Relational Operators
# a = 13
# b = 33
# print(a > b)  # a > b is False
# print(a < b)  # a < b is True
# print(a == b)  # a == b is False
# print(a != b)  # a != b is True
# print(a >= b)  # a >= b is False
# print(a <= b)  # a <= b is True
# ---------------------------------------------------------------------------

# Logical Operators
# and	Logical AND: True if both the operands are true	x and y
# or	Logical OR: True if either of the operands is true 	x or y
# not	Logical NOT: True if the operand is false 	not x

# Examples of Logical Operator
a = True
# b = False
# print(a and b)  # Print a and b is False
# print(a or b)  # Print a or b is True
print(not a)  # Print not a is False
# ---------------------------------------------------------------------------

# Bitwise Operators
# &	Bitwise AND	x & y
# |	Bitwise OR	x | y
# ~	Bitwise NOT	~x
# ^	Bitwise XOR	x ^ y
# >>	Bitwise right shift	x>>
# <<	Bitwise left shift	x<<

# Examples of Bitwise operators
# a = 10
# b = 4
# print(a & b)  # Print bitwise AND operation
# print(a | b)  # Print bitwise OR operation
# print(~a)  # Print bitwise NOT operation
# print(a ^ b)  # print bitwise XOR operation
# print(a >> 2)  # print bitwise right shift operation
# print(a << 2)  # print bitwise left shift operation
# ---------------------------------------------------------------------------

# Assignment Operators
# =	Assign value of right side of expression to left side operand 	x = y + z
# += Add AND: Add right-side operand with left side operand and then assign to left operand	a+=b     a=a+b
# -= Subtract AND: Subtract right operand from left operand and then assign to left operand	a-=b     a=a-b
# *= Multiply AND: Multiply right operand with left operand and then assign to left operand	a*=b     a=a*b
# /= Divide AND: Divide left operand with right operand and then assign to left operand	a/=b     a=a/b
# %= Modulus AND: Takes modulus using left and right operands and assign the result to left operand	a%=b     a=a%b
# //= Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a//=b     a=a//b
# **= Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a**=b     a=a**b
# &= Performs Bitwise AND on operands and assign value to left operand	a&=b     a=a&b
# |= Performs Bitwise OR on operands and assign value to left operand	a|=b     a=a|b
# ^= Performs Bitwise xOR on operands and assign value to left operand	a^=b     a=a^b
# >>= Performs Bitwise right shift on operands and assign value to left operand	a>>=b     a=a>>b
# <<= Performs Bitwise left shift on operands and assign value to left operand	a <<= b     a= a << b


# Examples of Assignment Operators
# a = 10
# b = a  # Assign value
# print(b)
# b += a  # Add and assign value
# print(b)
# b -= a  # Subtract and assign value
# print(b)
# b *= a  # multiply and assign
# print(b)
# b <<= a  # bitwise lishift operator
# print(b)
# ---------------------------------------------------------------------------

# Identity Operators
# is       True if the operands are identical
# is not   True if the operands are not identical
# a = 10
# b = 20
# c = a
# print(a is not b)
# print(a is c)
# print(a is not c)
# print(a is b)
# ---------------------------------------------------------------------------
# Membership Operators
# in        True if value is found in the sequence
# not in    True if value is not found in the sequence

# name = "Abdelrahman"
# print("s" in name)  # False
# print("s" not in name)  # True
# print("r" in name)  # True
# print("r" not in name)  # False

# friends = ["Abdelrahman", "Seif", "Abdullah"]
# print("Abdullah" in friends)  # True
# print("Osama" in friends)  # False
# print("Mahmoued" not in friends)  # True

# x = 24
# y = 20
# list = [10, 20, 30, 40, 50]
# print(x not in list)
# if (x not in list):
#     print("x is NOT present in given list")
# else:
#     print("x is present in given list")
# print(y in list)
# if (y in list):
#     print("y is present in given list")
# else:
#     print("y is NOT present in given list")
# ---------------------------------------------------------------------------

# Chaining comparison operators in Python
# x < y <= z is equivalent to x < y and y <= z,

# x = 5
# print(1 < x < 10)  # True
# print(10 < x < 20)  # False
# print(x < 10 < x*10 < 100)  # True
# print(10 > x <= 9)  # True
# print(5 == x > 4)  # True

# a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
# exp1 = a <= b < c > d is not e is f
# exp2 = a is d > f is not c
# print(exp1)
# print(exp2)


# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# tuple1 = (1, 2, 3)
# tuple2 = (1, 2, 3)
# print(list1 is list2)
# print(tuple1 is tuple2)
# x = 1
# y = 1
# print(hex(id(x)))
# print(hex(id(y)))
# print(hex(id(list1[0])))
# print(hex(id(list2[0])))
# print(hex(id(tuple1[0])))
# print(hex(id(tuple2[0])))
# print(hex(id(tuple1)))
# print(hex(id(tuple2)))
# y = 30
# print(hex(id(y)))
