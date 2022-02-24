# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = int(input())
first = num // 100
second = num // 10 % 10
third = num % 10
mult = first*second*third
print('Произведение цифр числа =', mult)
amount = first+second+third
print('Сумма цифр числа =', amount)
