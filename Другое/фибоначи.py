# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 13
#
# Задание необходимо решать через рекурсию



def fib(num):
    if num == 0 or num == 1:
        return 1
    return fib(num - 1) + fib(num - 2)

result = fib(7 - 1)
print(result)