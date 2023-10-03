# def calk1(a, b):
#     return a + b

# тоже самое
calk1 = lambda a, b: a + b


# def calk2(a, b):
#     return a * b

# и тоже самое
calk2 = lambda a, b: a * b


def math(op, x, y):
    print(op(x, y))


math(calk1, 5, 45)  # 10
math(calk2, 4, 60)  # 240
math(lambda a, b: a * b, 4, 60)  # 240

