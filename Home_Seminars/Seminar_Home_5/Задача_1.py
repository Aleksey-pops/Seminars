# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a
# в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.


def step(a, b):
    if b == 0:
        return 1
    return a * step(a, b - 1)


a = int(input('Введите число a: '))
b = int(input('Введите степень b: '))

print(step(a, b))


# def f(a, b):
#     if b == 0:
#         return 1
#     return a * f(a, b - 1)
#
#
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# print("Результат: ", f(a, b))
