# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

from random import sample


def create_list(m:int):
    spis_symb = []
    for i in range(m):
        symb = sample("abc", k=3)
        spis_symb.append("".join(symb))
    return spis_symb    


def del_symb(b:list, phrase:str):
    new_spis = []
    new_spis = [b[i] for i in range(len(b)) if not b[i] == phrase]
    return new_spis
    

k = int(input("Введите количество элементов в строке: "))
if k>0:
    a = create_list(k)
    c = "abc"
    print("Исходный список:\n", *a)
    print("Финальный список:\n", *del_symb(a, c))
else:
    print("The data is incorrect.")