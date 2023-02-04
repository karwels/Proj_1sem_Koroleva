# В матрице найти среднее арифметическое положительных элементов.

from random import randint
from functools import reduce

m, n = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ")] #задаем размер матрицы
matrix = [[randint(-11, 11) for _ in range(n)] for _ in range(m)]  # создаем матрицу
print('Исходная матрица:')
for i in matrix:
    print(*i)
def sum_matr(matr):  # вычисляем средние арифметическое положительных элементов
    num = (n for row in matr for n in row if n > 0)
    counts = reduce(lambda x, y: (x[0] + y, x[1] + 1), num, (0, 0))
    return counts[0] / counts[1] if counts[1] > 0 else None
print(f'Среднее арифметическое положительных элементов: {sum_matr(matrix)}')