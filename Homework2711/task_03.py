# Напишите программу, которая будет преобразовывать десятичное число в
# двоичное. Без использования встроенной функции преобразования,без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011


def dev_new(n):
    list_1 = []
    while n>=2:
        list_1.append(n%2)
        n = n//2
    else:
        list_1.append(n)

    temp = []
    d = len(list_1)
    for i in range(0,d):
        temp.append(list_1[d-1-i])
    return temp         
    
n = int(input("Введите число: "))    
b = dev_new(n)
print(*b)

