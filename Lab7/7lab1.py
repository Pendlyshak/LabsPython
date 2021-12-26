#Визначити суму від’ємних елементів матриці з парною сумою індексів.
matrix = [
    [3, 6, 7],
    [12, -4, -9],
    [-19, -5, 8]
]
s = 0
rows = 3
cols = 3

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] < 0 and i%2==0:
            s += matrix[i][j]
print("Сума від’ємних елементів матриці з парною сумою індексів: {0}".format(s))





