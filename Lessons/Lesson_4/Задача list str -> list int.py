# С клавиатуры вводится набор чисел, в качестве разделителя  используется пробел. Этот набор будет считан в качестве
# строки. Как превратить list str в list int.


data = '15 156 96 3 5 8 52 5'
print(data)

# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)