def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res


print(sum_str('q', 'w', 'z'))  # qwz
print(sum_str('q', 'w', 'z', 't', 'o', 'P'))  # qwztoP
print(sum_str('1', '8', '9'))