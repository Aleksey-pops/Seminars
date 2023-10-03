# Boolean(Bool)
# True
# False
# && (and) (и) - (конъюнкция) (логическое умножение)
# || (or) (или) - (дизъюнкция) (логическое сложение)
# not (отрицание)

print(5 > 7)  # False
print(int(5 < 7), ' = True')  # 1 True
print(int(5 > 7), ' = False')  # 0 False


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
