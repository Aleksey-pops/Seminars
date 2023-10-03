# Словари - неупорядоченые коллекции произвольных обьектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. в словаре для определения
# Элемента используется значение ключа(строка, число).

d = {}
print(type(d))  # <class 'dict'>
d = dict()
print(d)
d['q'] = 'qwerty'
print(d)  # {'q': 'qwerty'}
d['w'] = 'rtyuyui'
print(d)  # {'q': 'qwerty', 'w': 'rtyuyui'}
print(d['w'])  # rtyuyui

for i in d:
    # print(i)  # q w
    # print(d['w'])
    print('{}: {}'.format(i, d[i]))  #  q: qwerty
#                                       w: rtyuyui

for (k, v) in d.items():
    print(k, v) #   q qwerty
#                   w rtyuyui

print(d.items()) # кортежи элементов dict_items([('q', 'qwerty'), ('w', 'rtyuyui')])

del d['w']  # удаление элемента
print(d)  # {'q': 'qwerty'}
