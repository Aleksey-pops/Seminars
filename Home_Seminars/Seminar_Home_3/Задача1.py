# Требуется вычислить сколько раз встречается некое число k в масиве list_1.


list_1 = [1, 2, 3, 4, 5]
k = 3

col = 0
for i in list_1:
    if i == k:
        col += 1
print(col)