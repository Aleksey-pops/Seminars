def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


a = sum_numbers(6)
print(a)
print(sum_numbers(5))



def sum_numbers(n, y =  'Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


a = sum_numbers(6, 'qwerty') #  qwerty 21
print(a)
print(sum_numbers(5)) #  Hello  15
