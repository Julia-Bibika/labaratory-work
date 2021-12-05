"""
Дано типізований файл, який містить дійсні числа.
Видалити з цього файлу числа, що менші за середнє арифметичне усіх чисел
"""
import random
k_el = 0
my_sum = 0
n = int(input("Введіть кількість чисел: "))
a = [random.randint(0, 50) for i in range(n)]
with open('z1ar_average.txt', 'w') as file:
    file.write(' '.join(map(lambda el: str(el), a)))
with open('z1ar_average.txt') as file:
    line = file.readline()
    numbers = list(map(lambda el: float(el), line.split(sep=' ')))
    for el in range(len(numbers)):
        my_sum += numbers[el]
        k_el += 1
        if k_el == (len(numbers)):
            average = my_sum / k_el
    print(numbers)
with open('z1ar_average.txt', 'w') as file:
    numbers = list(filter(lambda el: el > average, numbers))
    file.write(' '.join(map(lambda el: str(el), numbers)))
print(numbers)


