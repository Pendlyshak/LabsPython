#Дано текстовий файл, який містить цілі числа. Визначити кількість парних елементів.
s = 0
with open('TD.txt', 'r') as f:
    r = f.readlines()
    print(r)
    for el in r:
        el = int(el)
        if el % 2 == 0:
            s += 1
    print(s)









""""s = 0
    for el in r:
        el = int(el)
        if el % 2 == 0:
            s += 1
    print(s)
"""""



