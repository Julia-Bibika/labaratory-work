import math
# Завдання 4
"""
Якщо A = C = N, то y = cos(A + C + N)
Якщо A < C = N, то y = cos(A * C * N)
Якщо A < C < N, то y = cos((A + C) * N)
У інших випадках y = 0
"""
A = int(input('Введіть А: '))
C = int(input('Введіть С: '))
N = int(input('Введіть N: '))
A_rad = math.radians(A)
C_rad = math.radians(C)
N_rad = math.radians(N)

if A == C == N:
    y = math.cos(A_rad + C_rad + N_rad)
    print('y = {0:.2f}'.format(y))
elif A < C == N:
    y = math.cos(A_rad * C_rad * N_rad)
    print('y = {0:.2f}'.format(y))
elif A < C < N:
    y = math.cos((A_rad + C_rad) * N_rad)
    print('y = {0:.2f}'.format(y))
else:
    print('y = 0')