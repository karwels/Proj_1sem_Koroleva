#Дан список размера N. Найти количество его промежутков монотонности  (то есть
#участков, на которых его элементы возрастают или убывают).
import random
N = random.randrange(2,31)
a = [random.randrange(1,11) for i in range(N)]
print("N = ", N)
print("Массив:")
print(a)
k = 0
f = True
for i in range(1,N):
    if a[i-1] > a[i] :
        if f:
            k += 1
            f = False
    else :
        f = True
print("Элементы убывают:",k)
c = 0
g = True
for i in range(1,N):
    if a[i-1] < a[i] :
        if g:
            c += 1
            g = False
    else :
        g = True
print("Элементы возрастают :",c)
print("Монотонные интервалы:",c+k)
