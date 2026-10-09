# wap to enter the coefficients of a quadratic equetion and findout the roots of the equivalent.
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b*b - 4*a*c

if d >= 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)

    print("Root 1 =", r1)
    print("Root 2 =", r2)
else:
    print("Roots are imaginary")