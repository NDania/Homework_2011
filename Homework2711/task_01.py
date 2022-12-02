# Задайте список, состоящий из произвольных чисел, количество задаёт
# пользователь. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample

def new_set(n):
    spis = sample(range(1,n+1), k=n)
    return spis

def find_sum(a):
    sum = 0
    for i in range(0,n,2):
        sum +=a[i]
    return sum

n = int(input("Введите кол-во чисел: "))
a = new_set(n)
print(a)
print(find_sum(a))