b = []
max = 0
n = int(input("Введіть кількість чисел: "))
for i in range(1, n+1):
    a = float(input("num {0}: ".format(i)))
    b.append(a)
    c = sorted(b)
print(c)
d = [a for a in c if a<0]
print(d)
max = d[-1]
print("Найбільше число з від'ємних чисел: {0} ".format(max))
