"""
Об’єкт “Стек” (реалізація стеку за допомогою одновимірного масиву цілих чисел)
поля:
для зберігання вершини стеку (номера останнього доданого елемента);
масив елементів;
методи:
виведення на екран;
додавання нового елементу;
видалення елементу;
знаходження суми елементів.
"""


class Stack:
    def __init__(self, elements, num_last_dod=0):
        self.num_last_dod = num_last_dod
        self.__elements = elements

    @property
    def get_elements(self):  # getter for elements
        return self.__elements

    def set_elements(self, val):  # setter for element
        for i in range(len(self.__elements)):
            if type(val) != int:
                raise Exception('Element should be integer type')
            self.__elements.append(val)

    def pop(self, key):  # видалення елементу
        self.__elements.pop(key)
        return self

    def append(self, value):  # додавання елементу в список
        if type(value) != int:
            raise Exception('Element should be integer type')
        self.__elements.append(value)
        return self

    def sum_elements(self):  # сума всіх елементів масиву
        return sum(self.__elements)

    def last_dod(self):  # знаходження останнього доданого елемента
        return self.__elements[-1]

    def __str__(self):
        return str(self.__elements)


a1 = Stack([3, 8, 10, 5, 7])
print(a1)
print(a1.sum_elements())
print(a1.append(6))
print(a1.last_dod())
print(a1.pop(3))
