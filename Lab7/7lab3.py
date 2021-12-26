matrix_A = [
   [3, 9, 10],
   [4, 6, -3],
   [-5, -1, 0]
]

vector_b = 10

for i in range(len(matrix_A)):
   matrix_C = []
   for j in range(len(matrix_A[i])):
      matrix_C.append((matrix_A[i][j]*vector_b))
      if len(matrix_C)==3:
          print(matrix_C)