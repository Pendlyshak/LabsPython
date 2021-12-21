"n - кількість змінних"
"a - значення знаменника"
"b - значення чисельник"
"c - степінь"
"z - спільне число, яке виноситься за дужки"
"x - елементи"
import math
from math import sin
from math import factorial
n=int(input("Введіть значення n: "))
for i in range(1,n+1):
    x=int(input("Введіть значення {0}: ".format(i)))
a=factorial(2*n-1)
b=x**2
c=n-1
z=-1
d=(z**c)*((b**c)/factorial(a))
suma=0
if d<1:
    suma+=d
    sinx=suma
    print(sinx)
