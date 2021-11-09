import random
# Задача 11
# У векторі x всі елементи, які більші за середнє арифметичне замінити нулями.
# d - індексатор кожного елементу
n = int(input('Кількість елементів вектора х: '))
x = []
sum = 0
d = 0
for i in range(n):
    num_x = random.randint(-10, 10)
    x.append(num_x)
    sum += num_x
print("x = {0}".format(x))
print("sum = {0}".format(sum))
average = sum / n
print("average = {0}".format(average))
for d in range(n):
    if x[d] > average:
        x[d] = 0
print('x = {0}'.format(x))