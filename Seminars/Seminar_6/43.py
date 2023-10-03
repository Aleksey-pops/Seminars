# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2
import random


def get_random_array(array_len: int) -> int:
    """
    Получение случайного масива

    :param array_len: Размерность массива
    :return: Список цифр
    """
    return [random.randint(0, 10) for _ in range(array_len)]


def get_doubles(array):
    count = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] == array[i]:
                count += 1
    return count


if __name__ == "__main__":
    n = random.randint(1, 20)
    # n = int(input('Введите размер масива: '))
    array = get_random_array(array_len=n)
    print('Массив: ', array)
    print('Количество повторений: ', get_doubles(array=array))

# или
# def array(n):
#     return [random.randint(0, 9) for _ in range(n)]
#
#
# n = random.randint(1, 10)
# for i in range(n):
