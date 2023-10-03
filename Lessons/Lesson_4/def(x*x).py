def f(x):
    return x * x


x = int(input("Введите число: "))
print(f(x))
print(type(f))  # <class 'function'>
a = f
print(a(x))
print(type(a))  # <class 'function'>

