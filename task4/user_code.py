from math import *

def quadratic_equation(a,b,c):





    d = b**2 - (4 * a * c)

    if d < 0:

        return "No roots"

    elif d == 0:

        x = -(b / (2 * a))

        return x

    elif d > 0:

        x1 = (-b + sqrt(d)) / (2 * a)

        x2 = (-b - sqrt(d)) / (2 * a)

        return min(x1, x2), max(x1,x2)

        