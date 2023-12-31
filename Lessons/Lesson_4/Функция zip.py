# Функция zip() применяется к наборуитерируемых обьектов и возвращает итератор с кортежами из элементов входных данных.

# zip([1, 2, 3], ['о', 'д', 'т'], ['f', 's', 't'])
# [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# 2 пример

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]
