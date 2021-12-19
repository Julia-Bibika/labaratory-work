# Завдання 3. Задача 11
# Знайти вектор c=2<a,b>с-3*b, де a,b,c, <x,y> – скалярний добуток векторів.
"""
 dob_sk - скалярний добуток
 sum - сумма
"""
n = int(input('Введіть кількість елементів: '))
sum = 0
sum_1 = 0
sum_2 = 0
sum_3 = 0
a = []
b = []
c = []
for i in range(n):
    num = int(input('Вектору a number #{0} = '.format(i)))
    a.append(num)
for i in range(n):
    num_1 = int(input('Вектору b number #{0} = '.format(i)))
    b.append(num_1)
for i in range(n):
    num_2 = int(input('Вектору c number #{0} = '.format(i)))
    c.append(num_2)
for i in range(n):
    dob_sk = a[i] * b[i]
    sum += dob_sk
for i in range(len(c)):
    num_3 = (2 * sum * c[i]) - (3 * b[i])
    c.insert(i, num_3)
    c.pop(i + 1)
print("Вектор c = {0}".format(c))
