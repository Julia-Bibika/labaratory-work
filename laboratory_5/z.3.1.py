"""
Перевірити справедливість рівності при заданій точності Е:
1/1-x = 1 + x + x^2 + ... + x^n + ..., x є (-1;1)
"""
# 0 Позначення
"""
sum - сума
identity(тотожність) - 1/1-x
n - кількість елементів
c - степінь
"""
x = float(input("Введіть число від -1 до 1 : "))
n = int(input("Введіть кількість степенів : "))
eps = float(input("Введіть точність : "))
identity = 1/(1-x)
sum = 1
for i in range(n):
    while sum > eps:
        sum += x
        x *= x
        if identity == sum:
            print("Справедливість є рівною")
        print("sum = {0}".format(sum))
if identity == sum:
    print("Справедливість є рівною")
print("sum = {0}".format(sum))

