import math
# Використовуючи підпрограму для знаходження коренів квадратного рівняння
# Знайти розв’язок наступної системи рівнянь
"""
ax^2 + 2x + 7 = 0
bx^2 - 5x + 2 = 0
"""
a = int(input('Введіть а: '))
b = int(input('Введіть b: '))


def solution_a(a):
    n = 2
    c = 7
    d_a = (n ** 2) - (4 * a * c)
    if d_a < 0:
        d_a = "не існує"
        return d_a
    else:
        d_a = math.sqrt(d_a)
        return int(d_a)


def solution_b(b):
    n = 5
    c = 2
    d_b = (n ** 2) - (4 * b * c)
    if d_b < 0:
        d_b = "не існує"
        return d_b
    else:
        d_b = math.sqrt(d_b)
        return int(d_b)


def roots_a(a, solution_a):
    if solution_a(a) == "не існує":
        x1 = 0
        x2 = 0
        return x1, x2
    n = 2
    c = 7
    x1 = ((n - solution_a(a)) / (2 * a * c))
    x2 = ((n + solution_a(a)) / (2 * a * c))
    return x1, x2


def roots_b(b, solution_b):
    if solution_b(b) == "не існує":
        x1 = 0
        x2 = 0
        return x1, x2
    n = 5
    c = 2
    x1 = ((n - solution_b(b)) / (2 * b * c))
    x2 = ((n + solution_b(b)) / (2 * b * c))
    return x1, x2


res_a = solution_a(a)
res_b = solution_b(b)
decision_a = roots_a(a, solution_a)
decision_b = roots_b(b, solution_b)
print("Дискримінант в першому прикладі: {0}".format(res_a))
print("Дискримінант в другому прикладі: {0}".format(res_b))
print(decision_a)
print(decision_b)
