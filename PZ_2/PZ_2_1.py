#Даны целые положительные числа A и B (A > B). На отрезке длины
#A размещено максимально возможное количество отрезков длины B (без наложений).
#Используя операцию взятия остатка от деления нацело, найти длину незанятой части
#отрезка A.
a=int(input('Введите длину отрезка A '))
b=int(input('Введите длину отрезка B '))
if a>b:
    print('Длина незанятой части отрезка А =' , a%b)
else:
    print('Ошибка')
