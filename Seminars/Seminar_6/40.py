# Требуется вычислить, сколько раз встречается некоторое
# число k в массиве list_1.
#
# Найдите количество и выведите его

list_1 = [1, 2, 3, 4, 5, 4, 3]
# k = 3
# 1
col = 0
k = int(input('Введите число которое нужно найти: '))
for i in list_1:
    if i == k:
        col += 1
print(k)
print(i)

list_1 = [1, 2, 3, 4, 5, 2]
k = 2

# Введите ваше решение ниже
col = 0
for i in list_1:
    if i == int(k):
        col += 1
# print(k)
print(col)

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)