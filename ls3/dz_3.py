# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
n = int(input())
arr = []
for i in range(n):
    arr.append(random.randrange())

n_min = min(arr)
n_max = max(arr)
i_max = arr.index(n_max)
i_min = arr.index(n_min)
arr[i_max] = n_min
arr[i_min] = n_max

print(arr)
