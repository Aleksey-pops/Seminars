def summa_str(*args):
    res = ''
    for i in args:
        res += i
    return res


print(summa_str('trgfrvgrevf'))
print(summa_str('w', 'e', 'r', 'T'))
print(summa_str('w', 'e', 'r', 'T', 'P', 'OO'))
print(summa_str('1', '2', '3'))
