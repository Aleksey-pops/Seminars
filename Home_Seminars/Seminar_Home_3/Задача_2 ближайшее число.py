# Требуется найти в масиве list_1 самый близкий элемент к заданому числу л и вывести его.

list_1 = [1, 2, 3, 4, 24]
k = 14

num1 = num2 = k
while num1 not in list_1 and num2 not in list_1:
    num1 -= 1
    num2 += 1
    if num1 in list_1:
        print(num1)
    if num2 in list_1:
        print(num2)
if k in list_1:
    print(k)

# 2 вариант

res = [abs(list_1[i] - k) for i in range(len(list_1))]

x = res.index(min(res))

print(f'Список, {list_1}')
print(f'Введеное число: {k}')
print(f'Ближайшее число: {list_1[x]}')

# 3 вариант


min_div = abs(list_1[0] - k)
min_i = 0
for i in range(1, len(list_1)):
    cur_div = abs(list_1[i] - k)
    if cur_div < min_div:
        min_div = cur_div
        min_i = i

print(list_1[min_i])
