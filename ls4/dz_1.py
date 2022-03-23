# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import numpy as np


def manually():
    arr = [
        [14, -4, -12, 19, 1],
        [16, -6, 8, 7, 11],
        [11, 2, -5, 1, 20],
        [14, -4, -17, 15, 10]
    ]
    temp = [[],
            [],
            [],
            [],
            [],
            ]
    a = []

    for c in range(0, 5):
        for i in arr:
            temp[c].append(i[c])

    for i in temp:
        a.append(min(i))

    return max(a)


def np_rot():
    arr = [
        [14, -4, -12, 19, 1],
        [16, -6, 8, 7, 11],
        [11, 2, -5, 1, 20],
        [14, -4, -17, 15, 10]
    ]
    a = []
    arr2 = np.rot90(arr)

    for i in arr2:
        a.append(min(i))

    return max(a)


if __name__ == "__main__":
    print(manually())
    print(np_rot())

# В среднем использование функции rot модуля numpy замедляет работу скрипта в 5 раз:

# PS D:\GitHub\Homework_py_2\ls4> python -m timeit "from dz_1 import manually; manually()"
# 50000 loops, best of 5: 4.05 usec per loop
# PS D:\GitHub\Homework_py_2\ls4> python -m timeit "from dz_1 import np_rot; np_rot()"
# 10000 loops, best of 5: 22 usec per loop
