"""
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
"""

quantity = int(input('Введите количество элементов: '))

custom_list = []

for i in range(quantity):
    number = int(input('Введите число: '))
    custom_list.append(number)

custom_list.sort()
print(custom_list)