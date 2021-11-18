"""
Коефіцієнти системи лінійних рівнянь задані у виді прямокутної матриці.
Знайти кількість рядків матриці, середнє арифметичне елементів яких менше за задану величину.
"""
import random
A = []
b = int(input("Введіть кількість рядків матриці : "))
c = int(input("Введіть кількість стовбців матриці : "))
n = int(input("Введіть величину: "))
sum = 0
k_el = 0
average = 0
k_r = 0
for i in range(b):
    A.append([random.randint(-10, 20) for j in range(c)])
print(A)
for i in range(len(A)):
    for j in range(len(A)+1):
        sum = sum + A[i][j]
        k_el += 1
        if k_el == len(A[i]):
            average = sum / k_el
            k_el = 0
            sum = 0
            if average < n:
                k_r += 1
print("Кількість рядків матриці, середнє арифметичне елементів яких менше за {0}: {1}".format(n, k_r))
