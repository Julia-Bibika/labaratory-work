import random
"""
Коефіцієнти системи лінійних рівнянь задані у виді прямокутної матриці.
За допомогою допустимих перетворень звести матрицю до трикутного виду.
"""
A = []
s = []
new_el = []
b = int(input("Введіть кількість рядків матриці : "))
c = int(input("Введіть кількість стовбців матриці : "))
z = 1
for i in range(b):
    A.append([random.randint(-5, 7) for j in range(c)])
print(A)
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j] == 0:
            row_n = i + 1
            while row_n < len(A) and A[row_n][i] == 0:
                row_n += 1
            if row_n < len(A):
                A[i], A[row_n] = A[row_n], A[i]
        if A[i][j] != 0:
            for r in range(i + 1, len(A)):
                if A[r][i] != 0:
                    m = - A[r][i] / A[i][i]
                    for j in range(i, len(A)):
                        A[r][j] = (A[i][j] * m) + A[r][j]

print(*A, sep='\n')
