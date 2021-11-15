"""
Побудувати прямокутну матрицю А, елементи якої задаються формулою:
a_ij = i**j - j**i
Обчислити суму додатних елементів елементів матриці А.
"""
m = []
sum_dot = 0
b = int(input('Рядки: '))
c = int(input('Стовпці: '))
for i in range(b):
    m.append([((i ** j) - (j ** i)) for j in range(c)])
print(m)
for i in range(b):
    for j in range(c):
        if m[i][j] > 0:
            sum_dot = sum_dot + m[i][j]
print("Сума додатних елементів матриці з непарною сумою індексів : {0:.2f}".format(sum_dot))
