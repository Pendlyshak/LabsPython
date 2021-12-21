n = int(input("Введіть значення i: "))
def variable(i):
    if i == 0 or i == 1:
        return 1
    else:
        return (i-1)+(i-2)
print(variable(n))
