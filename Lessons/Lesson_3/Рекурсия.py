# Рекурсия - это функция которая вызвает сама себя.
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


a, b = 0, 1
list_1 = [0]
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)
