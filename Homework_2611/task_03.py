# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# in 
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

spis = []
n = int(input("Введите список чисел: "))
a = 1
sum = 0
for i in range(1, n+1):
    a = (1 + 1/i)**i
    sum+=a
    spis.append(round(a,3))
print(spis)
print(round(sum,3))
