# Задание№2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях
# первого массива стоят четные числа.
import random

array = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {array}')
even_number = []

for n in array:
    if n % 2 == 0:
        even_number.append(array.index(n))

print(f'Индексы чётных элементов массива: {even_number}')
