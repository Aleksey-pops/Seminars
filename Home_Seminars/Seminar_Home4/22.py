# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def element(x):
    h = []
    for _ in range(x):
        number = int(input(f'Введите элементы {x} набора: '))
        h.append(number)
    return h


def list_intersection(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result


n = int(input('Введите количество элементов первого набора чисел: '))
m = int(input('Введите количество элементов второго набора чисел: '))
v = element(n)
v1 = element(m)
print(v)
print(v1)

print(sorted(list_intersection(v, v1)))


# n = int(input('Введите количество элементов первого набора чисел: '))
# m = int(input('Введите количество элементов первого набора чисел: '))
# h = []
#
# for _ in range(n):
#     number = (input('Введите элементы:'))
#     h.append(number)
# print(h)
# h = set(h)
# h = list(h)
# h.sort()
# print(h)


# def element(n, m):
#     for _ in range(n):
#         number = (input('Введите элементы:'))
#         h.append(number)
#     return (n, m)



# # бесконечный цикл ввода с клавиатуру чисел
# numbers = []
# while True:
#     number = input("Введите число или введите 'stop' для окончания: ")
#     if number == 'stop':
#         break
#     numbers.append(int(number))
# print(numbers)
