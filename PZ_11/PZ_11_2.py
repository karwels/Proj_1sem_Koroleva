# Из предложенного текстового файла (text18-10.txt) вывести на экран его содержимое, количество букв в верхнем
# регистре. Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив после
# последней строки автора и название произведения.

f1 = open('text18-10.txt', 'r', encoding='UTF-8', errors='ignore').read()  # открываем файл на чтение

up = ' '.join([i for i in f1 if i.isupper()]).split(' ')  # получаем все буквы верхнего регистра

print(f'Содержимое файла: \n\n{f1}\n\nКоличество букв в верхнем регистре: {len(up)}')  # вывод
f2 = open('text18-10_2.txt', 'w', encoding='UTF-8')  # открываем файл на запись

author = 'М.Ю. Лермонтов'  # автор
title = 'Бородино'  # название произведения
f2.write(f1 + f'\n\nАвтор: {author}\nНазвание произведения: {title}')  # записываем в конец автора и название
f2.close()  # закрываем файл
