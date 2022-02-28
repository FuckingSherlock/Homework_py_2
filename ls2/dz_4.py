# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


n = int(input())
earlier = 1
result = 0
for i in range(n+1):
    result += earlier
    earlier /= -2
print(result)
