import random
import math

"""
Використовуючи відповідні підпрограми, з’ясувати, що є більшим.
Cереднє арифметичне чи середнє геометричне чисел.
 """


def ar_mean(a, sum=0, average=1):
    k_el = 0
    for i in range(len(a)):
        sum += a[i]
        k_el += 1
        average = sum / k_el
    return int(average)


def geom_mean(a, dob=1):
    for i in range(len(a)):
        dob *= a[i]
    dob = math.sqrt(dob)
    return int(dob)


k = ar_mean
k_1 = geom_mean


def por(k, k_1):
    if k > k_1:
        max_my = k
    else:
        max_my = k_1
    return max_my


a = []
n = int(input("Введіть кількість чисел: "))
for i in range(n):
    num = random.randint(0, 50)
    a.append(num)
print(a)
print(ar_mean(a, sum=0, average=1))
print(geom_mean(a, dob=1))
print(por(ar_mean(a, sum=0, average=1), geom_mean(a, dob=1)))
