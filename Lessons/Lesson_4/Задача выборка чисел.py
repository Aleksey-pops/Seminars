# s = [1, 2, 3, 5, 8, 15, 23, 38]
# for i in s:
#     if i % 2 == 0:
#         print([i, i * i])

# 2 вариант
# s = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
#
# for i in s:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
# print(res)

def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


s = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, s)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))
print(res)


# 2 вариант

s = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, s)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

# 3 вариант

s = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, s)
res = filter(lambda x: x % 5 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)