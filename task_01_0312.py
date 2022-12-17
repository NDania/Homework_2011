# Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

from decimal import Decimal

def accury_n(x, y):
    b = Decimal(f'{x}')
    return b.quantize(Decimal(f'{y}'))

a = float(input("Введите действительное число: "))
d = float(input("Введите требуемую точность в формате 0.0001: "))
print(accury_n(a, d))
