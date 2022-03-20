# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

counter = [0]*8
iter = 0

for i in range(2, 100):
    for n in range(2, 10):
        if i % n == 0:
            counter[n-2] += 1

while iter < len(counter):
    print(f'Количество чисел, кратных {iter+2} - {counter[iter]}')
    iter += 1
