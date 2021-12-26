from math import *
a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
x = int(input("Введіть значення x: "))

def suma(num):
    for el in range(a):
        if x > 3:
            suma = sin(x) + sin(x) ** el
            return suma
        else:
            suma = 15 + tan(x)
            return suma

def get_max(num1, num2):
    if num1 > num2:
        max = num1
    else:
        max = num2
    return max

u = max(suma(a), suma(b))
print("U = {0}".format(u))








