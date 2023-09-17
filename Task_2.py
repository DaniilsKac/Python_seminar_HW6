print('\nЗадача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)')
from random import randint

minValue = int(input("\nВведите минимальное значение массива: "))
maxValue = int(input("Введите максимальное значение массива: "))
massiveVolume = int(input("Введите кол-во элементов массива: "))
minToFind = int(input("Введите мин. значение диапазона: "))
maxToFind = int(input("Введите макс. значение диапазона: "))

list_1 = [randint(minValue, maxValue) for _ in range(massiveVolume)]
print(list_1)

for i in range(len(list_1)):
    if minToFind <= list_1[i] <= maxToFind:
        print(i, end=' ')
