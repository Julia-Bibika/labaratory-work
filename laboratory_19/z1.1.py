"""
Текстовий файл, який містить цілі числа. Визначити суму додатних елементів.
"""
from functools import reduce
import random
n = int(input("Введіть кількість чисел: "))
a = [random.randint(-50, 50) for i in range(n)]
with open('z1text_dod.txt', 'w') as file:
    file.write(' '.join(map(lambda el: str(el), a)))
with open('z1text_dod.txt') as file:
    line = file.readline()
    numbers = (map(lambda el: int(el), line.split(sep=' ')))
    s = reduce(lambda prevSum, el: prevSum + el, filter(lambda el: el > 0, numbers), 0)
    print(s)

