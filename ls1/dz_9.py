# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

nums = [int(input()), int(input()), int(input())]

max_num = max(nums)
min_num = min(nums)

for i in nums:
    if i != min_num and i != max_num:
        print('Среднее число = ', i)
