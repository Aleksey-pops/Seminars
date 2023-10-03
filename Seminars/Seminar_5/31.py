# Задача №31. Общее обсуждение
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1, ..., an , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fib(num):
    if num == 0 or num == 1:
        return 1
    return fib(num - 1) + (fib(num - 2))
    print(fib(num))

a = int(input('Введите число: '))
result = fib(a)
print(result)


# # факториал n! = (n -1)! * n, n>=1 ; 0! ==1
#
# def factorial(n):
#     if (n == 0):
#         return 1
#     return factorial(n - 1) * n
#
#
# n = int(input('Введите число: '))
# print(factorial(n))
#
#
# # Алгоритм Эвклида HOD(a,b) ; (НОД(b,a mod b) ; b!=0
#
# def gcd(a, b):
#     if (b == 0):
#         return a
#     return gcd(b, a % b)
#
#
# a = int(input('Введите число a:'))
# b = int(input('Введите число b:'))
# print('Найбольший делитель кратность> ', gcd(a, b))
#
#
# # Возведение в степень a ** n = a* a**(n-1), n>0 1, n=0 для n четное (a**2)**n/2
#
# def fast_power(a, n):
#     if (n == 0):
#         return 1
#     if (n % 2 == 1):
#         return a * fast_power(a, n - 1)
#     else:
#         return fast_power(a * a, n / 2)
#
#
# a = int(input('Введите число a:'))
# b = int(input('Введите степень числа b:'))
# print(fast_power(a, b))
#
#
# # числа фибоначи F: bn =
#
# def fib(n):
#     if (n <= 1):
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# x = int(input('Введите число фибоначи до которого нужно вычислить: '))
# print(fib(x))
