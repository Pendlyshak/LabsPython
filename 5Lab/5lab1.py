from math import *
a0=4
for i in range(1,13):
    s=a0-cos((a0**i)/12)
    a0=s
print(a0)
