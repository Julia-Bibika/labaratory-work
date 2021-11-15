"""
Дано матрицю A.Перевірити, чи є дана матриця діагональною матрицею.
"""
A = []
i = int(input("Введіть кількість рядків матриці : "))
j = int(input("Введіть кількість стовбців матриці : "))
for x in range(i):
    A.append([int(input("Введіть number#{0}{1} : ".format(x, y))) for y in range(j)])
print(A)
for x in range(i):
    for y in range(j):
        if x == y and A[x][y] != 0:
            print("Матриця A є діагональною матрицею")
        else:
            break
print("Матриця A не є діагональною матрицею")
