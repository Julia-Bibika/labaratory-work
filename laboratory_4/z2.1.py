# Задача 1. Дано два дійсних числа: а і b
# З'ясувати, чи належать ці числа інтервалу [1;2] U [3;7]
a = float(input('Введіть значення а: '))
b = float(input('Введіть значення b: '))
if 1 <= a <= 2 or 3 <= a <= 7:
    print("Число {0} належить проміжку [1:2] U [3:7]".format(a))
else:
    print("Число {0} не належить проміжку [1:2] U [3:7]".format(a))
if 1 <= b <= 2 or 3 <= b <= 7:
    print("Число {0} належить проміжку [1:2] U [3:7]".format(b))
else:
    print("Число {0} належить проміжку [1:2] U [3:7]".format(b))