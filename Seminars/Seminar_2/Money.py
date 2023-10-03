# Задачка монетки орел решки

s = 'OPOPOPOOOPPOPPOPPPP'
n = 0
while 'P' * n in s:
    n += 1
print(n - 1)

print('PPPP' in s)
print('P' not in s)

# p = o = mp = mo = 0
#
# for i in range(len(s)):
#     if s[i] == 'P':
#         p += 1
# print(p)
