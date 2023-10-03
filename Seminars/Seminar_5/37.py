# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать
# циклы (даже для ввода и вывода).
#
# Input:    2 -> 3 4
# Output: 4 3

n = int(input("Введите количество чисел > "))

def print_numbers(n: int):
    if n == 0:
        return ""
    line = input("Введите число > ")
    return print_numbers(n - 1) + line + " "

print(print_numbers(n).strip())# strip убирает пробел с двух сторон


# Циклом было бы так просто :)

if __name__ == "__main__":
    n = int(input('Введите число n: '))
    text = ''
    for _ in range(n):
        text = input() + text
        print(text)