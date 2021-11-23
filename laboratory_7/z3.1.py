"""
Дано матрицю A.Перевірити, чи є дана матриця діагональною матрицею.
"""
A = []
i = int(input("Введіть кількість рядків матриці : "))
j = int(input("Введіть кількість стовбців матриці : "))
k = 0
c = 0
for x in range(i):
    A.append([int(input("Введіть number#{0}{1} : ".format(x, y))) for y in range(j)])
print(A)
for x in range(i):
    for y in range(j):
        if x == y:
            if A[x][y] != 0:
                k += 1
                if k == i:
                    print("Матриця A є діагональною матрицею")
        else:
            if A[x][y] != 0:
                c += 1
                if c == i:
                    print("Матриця A не є діагональною матрицею")
                    break