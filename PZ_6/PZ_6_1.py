# Дан список A размера N и целое число K (1 < K < N). Вывести элементы список с
# порядковыми номерами, кратными K: AK, A2*K, A3*K,...
# . Условный оператор не
# использовать.
import random
import math
N = random.randint(10, 20)
A = [random.randint(1, 10) for i in range(N)]
K = random.randrange(1, N)
print("N = ", N)
print("K = ", K)
print(A)
j = K
while j < N:
    print("{0} : {1}".format(j, A[j]))
    j += K
