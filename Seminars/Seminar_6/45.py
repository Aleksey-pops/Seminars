# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

def sum_div(num):
    s = 1
    for div in range(2, int(num ** .5) + 1):
        if num % div == 0:
            s += div + num // div
    return s


k = int(input('Введите число k: '))
result = []
for num1 in range(2, k):
    num2 = sum_div(num1)
    sum2 = sum_div(num2)
    if num1 == sum2 and num1 != num2:
        temp = (num1, num2)
        temp_result = min(temp),max(temp)
        if temp_result not in result:
            result.append((num1, num2))
for i_turple in result:
    print(i_turple)
    print(*i_turple)


# sum_temp = sum_div(num1)

# print(sum_div(k))

# k = int(input('Введите число k: '))
# result = []
# for num1 in range(2, k):
#     for num2 in range(num1 + 1, k):
#         sum1 = sum_div(num1)
#         sum2 = sum_div(num2)
#         if sum1 == sum2:
#             result = (result.append(num1, num2))
