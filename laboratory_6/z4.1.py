# 11. Стиснути масив, вилучивши з нього всі елементи, значення яких знаходиться в інтервалі.
# Місце яке звільнилось в кінці масиву заповнити нулями.
"""
x - Початковий список
y - Кінцевий список
"""
n = int(input('Кількість елементів масиву x: '))
a = int(input('Початок інтервалу: '))
b = int(input('Кінець інтервалу: '))
x = []
for i in range(n):
    num = int(input('number #{0} = '.format(i)))
    x.append(num)
for i in range(len(x)):
    if a <= x[i] <= b:
        x.insert(i, 0)
        x.append(x[i])
        x.pop(i + 1)
        x.pop(i)
print("x = {0}".format(x))

