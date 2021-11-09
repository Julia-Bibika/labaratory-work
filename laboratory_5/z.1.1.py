import math
# 11. Дано a є R, n є N. Знайти сумму
"""
n - доданки
average - частка доданку
sum - сума доданків
f - факторіал
a - знаменнник
d - (a + e)
e - змінна в знаменнику
i - змінна яка запам'ятовує d
"""
n = int(input('Введіть кількість доданків: '))
a = int(input("Введіть число a : "))
f = 1
a_step = a ** 2
b = 1
sum = 0
d = 0
e = 1
i = 1
# (a+1)
for b in range(1, n):
    f = math.factorial(b)
    b += 1
    a_step *= a
    d = (a + e)
    e += 1
    i *= d
    znam = a_step * i
    average = f / znam
    sum += average
print('Сума = {0:.4f}'.format(sum))
