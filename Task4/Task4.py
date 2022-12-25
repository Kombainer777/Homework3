# Напишите программу, которая будет преобразовывать десятичное число в двоичное
n = int(input('Введите десятичное число: '))
binar = []
while n != 0:
    el = n % 2
    n = n // 2
    binar.append(el)
binar.reverse()
print(*binar, sep='')