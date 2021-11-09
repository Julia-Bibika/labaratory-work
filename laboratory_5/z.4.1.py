import math
"""
Нехай x_0 = 2 , x_1 = 1, x_i = cosx_i_1 ** x_i_2  . Визначити x_n.
"""
x_0 = 2
x_1 = 1
i = int(input("Введіть номер елемента : "))
if i == 1:
    print(x_0)
elif i <= 2:
    print(1)
else:
    for j in range(3, i + 1):
        x_n = math.cos(x_0) ** x_1
        x_0 = x_1
        x_1 = x_n
        print("x_n = {0:.2f}".format(x_n))