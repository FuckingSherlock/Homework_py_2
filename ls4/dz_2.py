# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import math

# 2.1 Без использования «Решета Эратосфена»


def manually():
    def is_prime(x):
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return False
        return True

    # n = int(input('Введите номер числа: '))
    n = 1000
    c = 0
    num = 2

    while True:
        if is_prime(num):
            c += 1
            if c == n:
                break
        num += 1
    print(num)
    return num


# 2.2 Используя алгоритм «Решето Эратосфена»

def bit_sieve(n):
    if n < 2:
        return []
    bits = [1] * n
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if bits[i - 2]:                       # если i -- простое
            for j in range(i + i, n + 1, i):  # все кратные ему = 0
                bits[j - 2] = 0
    return bits


def eratosthenes():
    # k = int(input('Введите число: '))
    k = 1000
    # k-ое простое не превосходит 1,5 k ln( k ) при k > 1:
    sieve = bit_sieve(int(1.5*k*math.log(k)) + 1)
    i = 0
    while k:
        k -= sieve[i]
        i += 1
    print(i + 1)
    return(i + 1)


if __name__ == "__main__":
    print(manually())           # 5 loops, best of 5: 85.5 msec per loop
    print(eratosthenes())       # 200 loops, best of 5: 1.44 msec per loop
