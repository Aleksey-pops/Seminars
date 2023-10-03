# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
import random


def mass(c):
    m = random.randint(1, 16)
    for i in range(c):
        return m

def maxx(n):
    if len(n) == 0:
        return None
    First = n[0]
    for number in n:
        if number > First:
            First = number
    return First

def minn(n):
    if len(n) == 0:
        return None
    First = n[0]
    for number in n:
        if number < First:
            First = number
    return First


N = int(input('Введите количество арбузов: '))
s = []
for i in range(N):
    ves = int(mass(N))
    s.append(ves)
print(s)
print(maxx(s))
print(minn(s))
