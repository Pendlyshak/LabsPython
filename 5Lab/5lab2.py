#Дано n є N. Побудувати алгоритм для визначення найбільшої цифри у записі цього числа n.

#0
"n - змінне значення"

#Позначення
n=int(input())
maxi=0

#Обчислення
while n>0:
    s=n%10
    if s>=maxi:
        maxi=s
    n=n//10
print(maxi)