import cmath


def equationroots(a, b, c):

    discriminant = b * b - 4 * a * c
    sqrt_val = cmath.sqrt(discriminant)

    # checking condition for discriminant
    if discriminant > 0:
        print(" real and different roots ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))

    elif discriminant == 0:
        print(" real and same roots")
        print(-b / (2 * a))

    # when less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", (sqrt_val/(2*a)))
        print(- b / (2 * a), " - i", (sqrt_val/(2*a)))


# Driver Program
a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))


if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)
