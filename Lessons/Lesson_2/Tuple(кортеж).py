# Кортеж это неизменяемый список занимает мало помяти быстрее работает
# Создание пустого кортежа

t = ()
print(type(t))  # <class 'tuple'>
t = (1)
print(type(t))  # <class 'int'>
t = (1,)
print(type(t))  # <class 'tuple'>

v = [1, 2, 99]
print(v)  # [1, 2, 99]
print(type(v))  # <class 'list'>

v = tuple(v)
print(v)  # (1, 2, 99)
print(type(v))  # <class 'tuple'>

a, b, c = v
print(a, b, c)  # 1 2 99

t = (1, 2, 3, 5, 19,)
for i in t:
    print(i) # 1 2 3 5 19

for i in range(len(t)):
    print(t[i]) # 1 2 3 5 19

t[0] = 2 # TypeError: 'tuple' object does not support item assignment Выдает ошибку неизменяемый.

