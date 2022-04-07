# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

arr = [random.uniform(0, 50) for i in range(10)]


def merge_sort(spisok):
    if len(spisok) > 1:
        mid = len(spisok)//2
        left = spisok[:mid]
        right = spisok[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                spisok[k] = left[i]
                i += 1
            else:
                spisok[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            spisok[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            spisok[k] = right[j]
            j += 1
            k += 1
    return spisok


print(f'{arr}\n{merge_sort(arr)}')
