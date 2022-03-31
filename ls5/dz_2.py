# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import OrderedDict as od

hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

dec_to_hex = '0123456789ABCDEF'

hex_num1 = input('Введите первое число: ').upper()[::-1]
hex_num2 = input('Введите второе число: ').upper()[::-1]


def create_dict(num):
    keys = [i for i in range(len(num))]
    values = list(num)
    return dict(zip(keys, values))


def convert(num, translate):
    for i in num.keys():
        num[i] = translate[str(num[i])]
    for i in num.keys():
        num[i] = num[i]*(16**i)
    return sum(num.values())


def back_convert(n):
    result = ''
    while n > 0:
        result = dec_to_hex[n % 16] + result
        n = n // 16
    return result


dec_num1 = convert(od(create_dict(hex_num1)), hex_to_dec)
dec_num2 = convert(od(create_dict(hex_num2)), hex_to_dec)


res_mult = dec_num1 * dec_num2
res_sum = dec_num1 + dec_num2

print(f'В десятичной системе, сумма = {res_sum}, произведение = {res_mult}')


print(
    f'В шеснадцатеричной системе, сумма = {back_convert(res_sum)}, произведение = {back_convert(res_mult)}')
