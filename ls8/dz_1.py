# Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.


import hashlib


def substring_count(S):
    S = S.lower()
    length = len(S)
    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(S[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


S = input()
print(f'Количество различных подстрок в строке {S}: {substring_count(S)}')
