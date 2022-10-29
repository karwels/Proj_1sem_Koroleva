#Дано целое число N (> 0). Найти сумму N^2 + (N + 1)^2 + (N + 2)^2 + ... + (2N)^2
#обработка исключений
try:
  N = int(input())
except ValueError:
  print('Ошибка, введите число')
  N= int(input())
i=N
S = 0
#нахожение суммы
while  i<2*N+1:
    x = i**2
    S += x
    print(i," : ",x," : ",S)
    i=i+1
print("Sum = ",S)
