# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

arr = [[int(input()), int(input()), int(input())],
       [int(input()), int(input()), int(input())],
       [int(input()), int(input()), int(input())],
       [int(input()), int(input()), int(input())],
       [int(input()), int(input()), int(input())]
       ]

for i in arr:
    i.append(i[0]+i[1]+i[2])
print(f'{arr[1]}\n{arr[2]}\n{arr[3]}')
