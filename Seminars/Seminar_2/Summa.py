# Задайте список из нескольких чисел. Напишите программу
# которая найдет сумму элементов списка,
# стоящих на нечетной позиции.
import random

# Пример [2, 3, 5, 9, 3] -> на нечетных позициях 3 и 9, ответ 12

import random

x = [2, 3, 5, 9, 3]

print(sum(x[1::2]))


# range(1:20:4) выдает последовательность чисел от 1 до 20 с шагом 4