# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N для пустого списка, заполните числами в диапазоне
# [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

spis = []
n = int(input("Введите число n: "))
a = int(input("Введите номер первой позиции: "))
b = int(input("Введите номер второй позиции: "))
mult = 0
for i in range(-n,n+1):
    spis.append(i)
print(spis)

if a <= (n*2+1) >= b:
    mult = spis[a-1]*spis[b-1]
    print(mult)
else:    
    print("Такой(их) позиции(й) не существует.")