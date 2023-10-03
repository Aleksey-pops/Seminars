# Функция - это фрагмент программы, используемый многократно.

# def function_name(x):
# body line 1
# ....
# body line n
# optinal return

# Создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.

def sumNumbers(n, y ='Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print([i for i in range(1, n + 1)])
    # print(summa)
    return summa


# n = int(input('Введите число n: '))
# print(sumNumbers(n))
print(sumNumbers(10, 'hfjahfjk'))
