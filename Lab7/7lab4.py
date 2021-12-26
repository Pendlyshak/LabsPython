#Дана цілочислова квадратна матриця. Розмістити елементи парних рядків у порядку спадання.
matrix = [
    [3, 6, -1],
    [7, 11, -4],
    [2, -8, 22]
]
rows = 3
cols = 3
print(matrix)
for i in range(rows):
    for j in range(cols):
        if i%2==0:
            (matrix[i]).sort(reverse=True)
print(f"{matrix}")