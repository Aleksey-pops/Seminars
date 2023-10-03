# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = int(input('Введите число: '))
n = int(input('Введите число n: '))
i = 1
N = 1
while N <= n:
    N = N + N
    print(N)
    i += 1
    # print(f'{i} + {N} = ')
    # print(N)
print(i)


def fibonaci(num):
    a, b, i = 0, 1, 1
    while a <= num:
        if num == a:
            return i
        a, b, i = b, a + b, +1
    else:
        return i - 1


n = int(input('Введите число n: '))
v = fibonaci(n)
print(v)
