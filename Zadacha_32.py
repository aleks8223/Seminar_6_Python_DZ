# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
length = list(randint(-50, 50) for i in range(int(input('Введите количество элементов массива: '))))
print(length)
min = int(input('Введите заданный минимум: '))
max = int(input('Введите заданный максимум: '))
for i in range(len(length)):
    if length[i] >= min and length[i] <= max:
        length2 = i 
        print(length2, end = ' ')