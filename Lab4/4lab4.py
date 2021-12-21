#0
...
"x, y - деякі змінні"
...

#Введення даних
x=int(input("Введіть значення x: "))
y=int(input("Введіть значення y: "))

import math
from math import e
#Порівняння
if y<x:
    z=y*x
    z=math.floor(z)
    print("z={0}".format(z))
elif y>x:
    z=x*e**y
    z=math.floor(z)
    print("z={0}".format(z))