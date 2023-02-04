#  В матрице элементы третьей строки заменить элементами из одномерного динамического массива соответствующей размерности.

from random import randint

m, n = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ")] #задаем размер матрицы
matrix = [[randint(0,11) for _ in range(n)] for j in range(m)] #создаем матрицу
print('Исходная матрица:')
for i in matrix:
    print(*i)
matrix[2] = [randint(-100, 100) for o in range(n)] # заменяем элементы третьей строки
print('Полученная матрица:')
for i in matrix:
    print(*i)