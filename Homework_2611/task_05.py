# Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random
spis = []
spis_2 = []
idx = 0
n = int(input("Введите число n: "))
for i in range(0,n):
    spis.append(i)
print(spis)
for y in range(n):
    idx = random.randrange(len(spis))
    spis_2.append(spis[idx])
    spis.pop(idx)
print(spis_2)
   
