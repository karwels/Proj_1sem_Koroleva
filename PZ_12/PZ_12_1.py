# В последовательности на n целых чисел найти и вывести:
# 1. максимальный среди отрицательных
# 2. элементы кратные двум
# 3. их сумму
from random import randint #импортируем из библиотеки random функцию randint
n = [randint(-10, 10) for i in range(int(input('Введите количество чисел в последовательности: ')))]# создаем последовательность на n целых чисел
print(n)#выводим последовательность
print('Максимальный среди отрицательных: ', max([i for i in n if i < 0]))#ищем максимальное среди отрицательных
print('Элементы кратные двум: ',str([i for i in n if i % 2 == 0]))#ищем элементы кратные двум
print('Сумма элементов: ',str(sum(n)))#ищем сумму элементов