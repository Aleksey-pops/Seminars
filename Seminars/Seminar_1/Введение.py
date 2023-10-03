# Сервисы для тренировок
# acmp
# e-olymp(с vpn)
# codewars
# codeforce
# kaggle(для аналитиков)
# informatics


# Статические (C#, C++, C, Java, Delphi ...)
# Динамические (Python, Javascript)

n = input('Введите данные: ')  # 5
print(n * 5)  # 55555
print(int(n) * 5)  # 25

# int()
# str()
# float()
# bool()

print(int('2408') + 2)  # 2410
print(int(14.99))  # 14

n = int(input('Введите число: '))  # 5
print(f'{n} * 2 = {n * 2}')  # 5 * 2 = 10

print(str(n) * 2)  # 55
print(str('123.4' * 2))  # 123.4123.4
# print(str('123.4' + 2))  # print(str('123.4' + 2)) TypeError: can only concatenate str (not "int") to str

n = float(input('Введите дробное число: '))  # 4.44
print(n * 3)  # 13.32
print(float(5))  # 5.0

print(5 // 2)  # 2 целочисленое деление
print(5 / 2)  # 2.5  Деление с дробной частью
print(5 % 2)  # 1 остаток от деления

# Boolean(Bool)
# True
# False
# && (and) (и) - (конъюнкция) (логическое умножение)
# || (or) (или) - (дизъюнкция) (логическое сложение)
# not (отрицание)

print(5 > 7)  # False
print(int(5 < 7), ' = True')  # 1 True
print(int(5 > 7), ' = False')  # 0 False
print(-12 // 5)  # -3

# n = int(input('Введите число: '))  # 10
# if n > 7 and n < 12:
#     #    1    *     1    =    1 (True)
#     print('yes')
# else:
#     print('no')

n = int(input('Введите число: '))  # 11
if n > 7 and n < 9 or n > 10:
    #    1   *      0   +  1     =   1 (True)
    print('yes')
else:
    print('no')