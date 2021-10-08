import numpy as np

print("Введите количество столбцов матрицы 1: ")
j = int(input())

print("Введите количество строк матрицы 1: ")
i = int(input())

ii = i
jj = j

Matrix1 = np.arange((i*j)).reshape(i, j)
print(Matrix1)

#------------------------------------------#

print("Введите количество столбцов матрицы 2: ")
j1 = int(input())

print("Введите количество строк матрицы 2: ")
i1 = int(input())

ii1 = i1
jj1 = j1


Matrix2 = np.arange(i1*j1).reshape(i1, j1)
print(Matrix2)


result = Matrix1.dot(Matrix2)
print("Результат умножения матриц: \n", result)


