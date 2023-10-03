# Хакер Василий получил доступ к классному журналу и хочет
# заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
#
# Output: 1 3 3 3 1

import random

n = int(input('Введите количество цифр: '))
list_1 = [random.randint(1, 5) for _ in range(n)]
print(list_1)

minNum = min(list_1)

maxNum = max(list_1)


def min_max_search(lst):
    minNum = lst[0]
    maxNum = lst[0]
    for num in lst[1:]:
        if num < minNum:
            minNum = num
        if num > maxNum:
            maxNum = num
    return minNum, maxNum


def change(minN, maxN, lst):
    for i in range(len(lst)):
        if lst[i] == maxN:
            lst[i] = minN
    return lst


minNum, maxNum = min_max_search(list_1)
print(minNum, maxNum)
print(change(minNum, maxNum, list_1))
