# Напишите программу, которая принимает на вход цифру, обозначающую
# день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Введите день недели: "))
if a > 7 or a < 1:
    print("Вы ввели некорректное число")
else:
    if a == 6 or a == 7:
        print("День выходной")   
    else:
        print("День выходным не является")
