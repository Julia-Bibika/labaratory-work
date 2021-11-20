import math
"""
Нехай x_0 = 0, x1 = x2 = x3 = 7
 x_i = (x(i-1)+ 4x(i-2)(1+x(i-2))+x(i-3))/(sqrt x(i-4)) + x(i-4).Визначити x_n.
"""


def create_x(i):
    if i == 0:
        return 0
    if i == 1 or i == 2 or i == 3:
        return 7
    else:
        x_i = (create_x(i - 1) + (4 * (create_x(i - 2)) * (1 + create_x(i - 2)) + create_x(i - 3))) / (
            math.sqrt(create_x(i - 3))) + create_x(i - 4)
        return (x_i)


i = int(input("Введіть номер елемента: "))
res = create_x(i)
print("{0}".format(res))
