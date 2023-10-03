# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10
import math


def find_farthest_orbit(list_of_orbits):
        areas = [math.pi * a * b for a, b in list_of_orbits if a != b]
        max_index = areas.index(max(areas))
        a, b = list_of_orbits[max_index]
        return a, b


list_of_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(list_of_orbits))


# Второй вариант

# def find_farthest_orbit(list_of_orbits):
#         pi = 3.14
#         pair = 0

#         list_of_orbits = [pair for pair in list_of_orbits if pair[0] != pair[1]]
#         areas_list = [pair[0] * pair[1] * pi for rair in list_of_orbits]
#         max_area = max(areas_list)
#         max_area_index = areas_list.index(max_area)
#         return list_of_orbits[max_area_index]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))