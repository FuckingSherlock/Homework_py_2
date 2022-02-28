# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

# 4.1
import string
from random import *

num = randrange(5, 50)
print(num)

# 4.2
num = triangular(12, 40)
print(num)

# 4.3
symb = choice(string.ascii_letters)
print(symb)
