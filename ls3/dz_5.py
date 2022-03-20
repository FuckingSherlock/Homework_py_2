# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

arr = [randint(-20, 20) for _ in range(10)]
print(arr)
counter = {}
ind = 0
for i in arr:
    if i < 0:
        counter.setdefault(i, ind)
    ind += 1

print(counter)
print(
    f'Элемент {max(counter.keys())} по индексу {counter[max(counter.keys())]}')
