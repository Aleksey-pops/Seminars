# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
import random

# n = int(input('Введите размер первого масива: '))
# m = int(input('Ведите размер второго масива:'))
#
# list_1 = []
# list_2 = []
#
# for i in range(n):
#     list_1[i] = random.randint(1, 10)
# for i in range(m):
#     list_2[i] = random.randint(1, 10)

# или другой вариант

n = random.randint(5, 10)
m = random.randint(5, 10)

list_1 =[random.randint(1, 10) for i in range(n)]
list_2 =[random.randint(1, 10) for j in range(m)]

print(n, list_1)
print(m, list_2)
list_3 = []
for num in list_1:
    if num not in list_2:
        list_3.append(num)
print(list_3)
# или
list_3 = [num for num in list_1 if num not in list_2]

print(list_3)