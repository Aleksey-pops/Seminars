# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# 1 Вариант

n1 = int(input('Введите сколько учеников в 1 классе: '))
n2 = int(input('Введите сколько учеников в 2 классе: '))
n3 = int(input('Введите сколько учеников в 3 классе: '))
p1 = n1 // 2 + n1 % 2
print('Столько парт надо в первый класс: ', p1)
p2 = n2 // 2 + n2 % 2
print('Столько парт надо в второй класс: ', p2)
p3 = n3 // 2 + n3 % 2
print('Столько парт надо в третий класс: ', p3)
print(f'Столько парт надо всего: {p1 + p2 + p3}')
print(n1 // 2 + n1 % 2 + n2 // 2 + n2 % 2 + n3 // 2 + n3 % 2)
# 2 Вариант
