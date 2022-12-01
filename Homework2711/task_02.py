# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import choices

def new_set(n):
    spis = choices(range(n), k=n)
    return spis

def mult_el(a):
    dop_sp = []
    pr = 0
    if n%2!=0:
        for i in range(0,n//2):
            pr = a[i]*a[n-1-i]
            dop_sp.append(pr)
        dop_sp.append(a[i+1])    
    else:
        for i in range(0,n//2):
            pr = a[i]*a[n-1-i]
            dop_sp.append(pr)
        
    return dop_sp

n = int(input("Введите кол-во чисел в списке: "))
a = new_set(n)
print(a)
print(mult_el(a))