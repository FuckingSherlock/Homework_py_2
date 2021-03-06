# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

from random import randint

arr = [randint(-100, 100) for i in range(10)]


def bubble_sort(spisok):
    for i in range(len(spisok) - 1):
        for j in range(len(spisok) - i - 1):
            if spisok[j] < spisok[j+1]:
                # Заменить "<" на ">" для сортировки по возрастанию.
                spisok[j], spisok[j+1] = spisok[j+1], spisok[j]
    return spisok


print(f'{arr}\n{bubble_sort(arr)}')

# Я позволил себе немного упростить это дело, т.к. в вашей реализации мне вообще ничего не понятно было...
# Еще и не работало как надо.
# По возрастанию нормально, а с убыванием беда.
# А эта реализация и выглядит понятнее, и переключить ее на обратную сортировку проще.
