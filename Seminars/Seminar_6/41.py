# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:         Ввод:
# 5               5
# 1 2 3 4 5     1 5 1 5 1
# Вывод:       Вывод:
# 0               2
import random

n = random.randint(5, 10)
# list_1 = []
# for _ in range(n):
#     list_1.append(random.randint(1, 10))
# или лист комприхейшенс

list_1 = [random.randint(1, 10) for _ in range(n)]
print(n, list_1)
count_nums = 0

for i in range(1, n - 1):
    if list_1[i - 1] < list_1[i] > list_1[i + 1]:
        count_nums += 1

print(count_nums)