"n - довжина масиву"
"ai - елементи масиву A"
"bi - елементи масиву B"
s=[]
dobutok=1
suma=0
n=int(input("Введіть довжину масиву: "))
import math
from math import sin
from math import factorial as f
for i in range(1,n+1):
    ai=(((i-1)**2)/((2*i**2)-1))+(f(i)*sin(i))
    print(round(ai, 1))
    for j in range(1,i+1):
        if ai<0:
            dobutok=dobutok*(ai)
            s.append(dobutok)
        else:
            suma+=i*abs(ai)
            s.append(suma)
print(s)