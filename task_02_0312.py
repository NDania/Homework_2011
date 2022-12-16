# Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]


def spis_simp_mult(n:int):
    spis=[]
    a=n
    k=2
    for i in range(n):
        while(a%k==0):
            spis.append(k)
            a=a//k
        k+=1    
    return spis

n = int(input("Введите целое положительное число: ")) 
if n <= 0:
    print("Число не натуральное.")
print(f'{spis_simp_mult(n)}')