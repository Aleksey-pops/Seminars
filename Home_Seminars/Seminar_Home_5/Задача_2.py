# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# Функция не должна ничего выводить, только возвращать значение.

def sum(a, b):
    if a == 0:
        return b
    else:
        return 1 + sum(a - 1, b)

a = int(input('Введите число a: '))
b = int(input('Введите степень b: '))

print(sum(a, b))