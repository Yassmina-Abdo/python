
# Q1 -------------------------------------------------------------------
from datetime import date
fname = input('Enter First Name: ')
Lname = input('Enter Last Name: ')
print('The reverse name is %s ' % fname[::-1] + ' ' + '%s' % Lname[::-1])
# Q1 -------------------------------------------------------------------


# Q2 -------------------------------------------------------------------
days = float(input('Enter days: '))
Hours = float(input('Enter Hours: '))
minuts = float(input('Enter mins: '))
seconds = float(input('Enter secs: '))
Sec = ((days*(60*60*24)) + (Hours*(60*60)) + (minuts*(60)) + (seconds))
print('The area of the triangle is %0.2f' % Sec)
# Q2 -------------------------------------------------------------------


# Q3 -------------------------------------------------------------------
list = ['Red', 'Green', 'White', 'Black']
print(list[0] + " " + list[-1])
# Q3 -------------------------------------------------------------------


# Q4 -------------------------------------------------------------------
d1 = date(2021, 8, 18)
d2 = date(2021, 10, 26)
count = d2 - d1
print(count.days)
# Q4 -------------------------------------------------------------------


# Q5 -------------------------------------------------------------------
name = 'Yasmina'
age = 22
address = 'Cairo'
print("my name is {} and my age is {} and my address {}".format(
    name, age, address))  # 1
print("my name is {:s} and my age is {:d} and my address is {:s}".format(
    name, age, address))  # 2
print('my name is %s ' % name + 'and my age is %d ' %
      age + 'and my address is %s' % address)  # 3
# Q5 -------------------------------------------------------------------


# Q6 -------------------------------------------------------------------
X = int(input('Enter X: '))
Y = int(input('Enter Y: '))
tmp = X
X = Y
Y = tmp
print('X value is {:d} Y value is {:d}'.format(X, Y))
# Q6 -------------------------------------------------------------------


# Q7 -------------------------------------------------------------------
base = float(input('Enter The base: '))
Height = float(input('Enter Height: '))

area = (base * Height) / 2
print('The area of the triangle is %0.2f' % area)
# Q7 -------------------------------------------------------------------


# Q8 -------------------------------------------------------------------
num = 1.2345
print(round(num, 2))
# Q8 -------------------------------------------------------------------
