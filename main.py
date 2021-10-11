import numpy as np

print("Выберите функцию: ")
print("1 - Матрица на матрицу")
print("2 - Матрица на вектор")
print("3 - Вектор на матрицу")


n = int(input())

def MatrixXMatrix():
    print("Введите количество столбцов матрицы 1: ")
    j = int(input())

    print("Введите количество строк матрицы 1: ")
    i = int(input())

    Matrix1 = np.random.randint(20, size=(i, j))
    print(Matrix1)

    # ------------------------------------------#

    print("Введите количество столбцов матрицы 2: ")
    j1 = int(input())

    print("Введите количество строк матрицы 2: ")
    i1 = int(input())

    Matrix2 = np.random.randint(20, size=(i1, j1))
    print(Matrix2)

    result = Matrix1.dot(Matrix2)
    print("Результат умножения матриц: \n", result)


def MatrixXVec():


    print("Введите количество столбцов матрицы: ")
    j = int(input())

    print("Введите количество строк матрицы: ")
    i = int(input())

    Matrix = np.random.randint(20, size=(i, j))
    print(Matrix, end="\n")

    print("Введите количество элементов вектора: ")
    ii = int(input())

    Vector = np.random.randint(20, size=(ii, 1))
    print(Vector, end="\n")

    print()
    if(ii == j):
        result = Matrix.dot(Vector)
        print(result, end="\n")
    else:
        print("Количество столбцов матрицы не равно количеству элементов вектора")

def VecXMatrix():

    print("Введите количество элементов вектора: ")
    jj = int(input())

    Vector = np.random.randint(20, size=(1, jj))
    print(Vector, end="\n")

    print("Введите количество столбцов матрицы: ")
    j = int(input())

    print("Введите количество строк матрицы: ")
    i = int(input())

    Matrix = np.random.randint(20, size=(i, j))
    print(Matrix, end="\n")


    print()
    if(i == jj):
        result = Vector.dot(Matrix)
        print(result, end="\n")
    else:
        print("Количество строк матрицы не равно количеству элементов вектора")

if (n == 1):
    MatrixXMatrix()
elif (n == 2):
    MatrixXVec()
elif (n == 3):
    VecXMatrix()