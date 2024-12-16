import math

def task1():
    """Задача 1: Обчислення виразу z"""
    a = float(input("Введіть значення кута a в радіанах: "))
    z = math.cos(a) + math.sin(a) + math.cos(3 * a) + math.sin(3 * a)
    print("Значення виразу z =", z)

def fibonacci(n):
    """Задача 2: Обчислення n-го числа Фібоначчі"""
    if n < 0:
        return
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def task2():
    n = int(input("Введіть номер числа Фібоначчі: "))
    result = fibonacci(n)
    print(f"{n}-е число Фібоначчі: {result}")

def task3():
    """Задача 3: Заміна рядків у матриці"""
    def swap_rows(matrix, row1, row2):
        matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]
    ]

    print("Початкова матриця:")
    for row in matrix:
        print(row)

    swap_rows(matrix, 0, 2)  # міняємо 1-й та 3-й рядки

    print("Матриця після заміни рядків:")
    for row in matrix:
        print(row)
