# Найдите сумму цифр трехзначного числа.



n = int(input('Введите трехзначное число: '))
print(n % 10 + (n // 10 % 10) + (n // 100))


