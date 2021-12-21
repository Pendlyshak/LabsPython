x0=0
x1=x2=9
n=int(input("Введіть значення n: "))
for i in range(1,n+1):
    if i>=3:
        s=x0+x1+x2
        x0=s
print(x0)