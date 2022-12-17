# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности
# в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from collections import Counter
from random import choices


def create_spis(n):
    return choices(range(1, n), k = n)


def pereb_spis(spis_pr):
    c = Counter(spis_pr)
    spis_ok = [i for i in spis_pr if c[i] ==1]
    return spis_ok       


n = int(input("Введите кол-во элементов в списке: "))
if n<0:
    print("Введено некорректное число.")
else:
    b = create_spis(n)   
    print(f'{b}')    
    c = pereb_spis(b)
    print(f'{c}')
    