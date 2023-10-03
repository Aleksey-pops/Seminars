# Требуется найти в массиве list_1 самый близкий по величине
# элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5, 6]
k = 6
# 5

for i in list_1:
    d = k - int(i)
    print(d)
    if min(d):
        print(d)




# def nearest_value(items, value):
#     '''Поиск ближайшего значения до value в списке items'''
#     found = items[0] # найденное значение (первоначально первое)
#     for item in items:
#         if abs(item - value) < abs(found - value):
#             found = item
#     return found
