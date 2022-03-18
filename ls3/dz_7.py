# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

arr = [randint(-20, 20) for _ in range(10)]
print(arr)
a = arr.pop(arr.index(min(arr)))
b = arr.pop(arr.index(min(arr)))
print(a, b)
