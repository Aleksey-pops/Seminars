# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6] same
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# def same_by(characteristic, objects):
#     if characteristic == objects:
#         return print(True)
#     return (False)


def same_by(characteristic, objects):
    result_list = list(filter(characteristic, objects))
    print(result_list)
    if objects == result_list or result_list == []:
        return True
    return False


values = [1, 3, 11, 9]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')


# def same_by(characteristic, objects):
#     if len(objects) == 0:
#         return True
#
#     unique_values = set(map(characteristic, objects)
#     return len(unique_values) == 1
#
# values = [1, 2, 10, 6]
# print(same_by(values[0], values[1]))


# def same_by(characteristic, objects):
#     result_list = []
#     for num in objects:
#         if characteristic(num):
#             result_list.append(num)
#     if objects == result_list or result_list == []:
#         return True
#     return False

# второй вариант
# def same_by(characteristic, objects):
#     result_list = list(map(characteristic, objects))
#     print(result_list)
#     if len(objects) == sum(result_list) or sum(result_list) == 0:
#         return True
#     return False