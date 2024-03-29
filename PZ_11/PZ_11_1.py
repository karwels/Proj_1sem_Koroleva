# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Элементы в обратном порядке:
# Сумма элементов последней половины:
print('17, 9, -3, 1, 2, 10, -4, 7, -2, -1', file=open('file_1.txt', 'w'))# Записываем  в файл данные
d = [int(i) for i in open('file_1.txt').read().split(', ')]   # Перебор файла запись целочисленных в список
l = open('file_new_1.txt', 'w')  # Создаём новый файл
print('Исходные данные:', open('file_1.txt').read(), file=l) # Выводим исходные данные
print('Количество элементов:', len(open('file_1.txt').read().split(', ')), '\n', file=l) # Считаем количество элементов
print('Элементы в обратном порядке:', d[::-1], '\n', file=l) #Выводим элементы в обратном порядке
print('Сумма элементов последней половины:', sum(d[5:]), file=l) # Считаем сумму элементов
l.close()  # Закрываем .txt файл