from random import randint
"""
Визначити кількість від’ємних елементів матриці з обома непарними індексами.
"""

i = int(input('Рядки: '))
j = int(input('Стовпці: '))
k = 0
m = [[randint(-10, 5) for x in range(j)] for y in range(i)]
print(m)
for x in range(i):
    for y in range(j):
        if x % 2 != 0 and y % 2 !=0:
            if m[x][y] < 0:
                k += 1
print("Кількість від’ємних елементів матриці з обома непарними індексами: {0}".format(k))
