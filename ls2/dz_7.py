# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.


n = int(input())
result = 0

for i in range(1, n+1):
    result += i

result2 = n * (n + 1) // 2
if result == result2:
    print(f'{result} = {result2}. Доказано!')
else:
    print(result)
    print(result2)
