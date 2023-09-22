from math import sqrt

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
d = b**2 - 4*a*c
print(d)
x1 = (-b - sqrt(d)) / 2*a
x2 = (-b + sqrt(d)) / 2*a
print(x1, x2)






