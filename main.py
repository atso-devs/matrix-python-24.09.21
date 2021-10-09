import numpy as np

def multipleMatrix():
    # Генерирование первой матрицы
    print("Введите количество столбцов матрицы 1: ")
    n1 = int(input())

    print("Введите количество строк матрицы 1: ")
    m1 = int(input())

    Matrix1 = np.arange((n1*m1)).reshape(n1, m1)
    print(Matrix1)

    # Генерирование второе матрицы
    print("Введите количество столбцов матрицы 2: ")
    n2 = int(input())

    print("Введите количество строк матрицы 2: ")
    m2 = int(input())

    Matrix2 = np.arange(n2*m2).reshape(n2, m2)
    print(Matrix2)

    ## Умножение матриц
    result = Matrix1.dot(Matrix2)
    print("Результат умножения матриц: \n", result)

def vekMulMatr():
    print("Введите количество элементов в векторе: ")
    nVek = int(input())
    vektor = np.random.randint(0, 10, nVek)
    print(vektor)
    
    print("Введите количество столбцов матрицы: ")
    n = int(input())

    print("Введите количество строк матрицы: ")
    m = int(input())

    matrix = np.arange((n*m)).reshape(n, m)
    print(matrix)

    total = vektor.dot(matrix)
    print(total)

def matrMulVek():
    print("Введите количество элементов в векторе: ")
    nVek = int(input())
    vektor = np.random.randint(0, 10, nVek)
    print(vektor)
    
    print("Введите количество столбцов матрицы: ")
    n = int(input())

    print("Введите количество строк матрицы: ")
    m = int(input())

    matrix = np.arange((n*m)).reshape(n, m)
    print(matrix)

    total = matrix.dot(vektor)
    print(total)

print("Выберите функционал: ")
print("1 - Умножение матриц")
print("2 - Умножение вектора на матрицу")
print("3 - Умножение матрицы на вектор")

num = int(input())

if (num > 3) and (num < 1):
    print("Введенные вами данные недопустимы. ")
else:
    if num == 1:
        multipleMatrix()
    elif num == 2:
        vekMulMatr()
    elif num == 3:
        matrMulVek()

