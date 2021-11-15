import random
"""
Циклічно зсунути парні рядки матриці зліва направо на k позицій.
"""
A = []
s = []
b = int(input("Введіть кількість рядків матриці : "))
c = int(input("Введіть кількість стовбців матриці : "))
k = int(input("Зсунути на скільки позицій: "))

for i in range(b):
    A.append([random.randint(-10, 10) for j in range(c)])
print(A)
j = 1
for j in range(c):
    for i in range(b):
        if j % 2 == 0:
            s = A[-k:] + A[:-k]
print(s)