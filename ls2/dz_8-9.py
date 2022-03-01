# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

find = input('Что ищем? ')
quantity = int(input('Сколько чисел? '))
nums = ''
nums_list = []

for _ in range(quantity):
    temp = input('Введите число: ')
    nums_list.append(temp)
    nums += temp

counter = nums.count(find)

print(counter)

# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

sum_list = []
for i in nums_list:
    sum_list.append(sum(map(int, str(i))))

max_num = max(sum_list)
print(
    f'Наибольшая сумма цифр у числа {nums_list[sum_list.index(max_num)]}: {max_num}')
