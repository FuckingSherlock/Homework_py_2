# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

arr = [randint(0, 20) for _ in range(100)]
counter = {}
print(f'Исходный массив: {arr} \n')

for i in arr:
    if i not in counter.keys():
        counter.setdefault(i, 0)
    else:
        counter[i] += 1

print(f'Подсчет: {counter} \n')
frequent_num = max(counter, key=counter.get)
print(f'Число {frequent_num} встречается {counter[frequent_num]} раз')
