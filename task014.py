# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = abs(int(input('Введите число n ')))
stop = 0
num = 2
for i in range(n):
    if stop != 1:
        num = num ** i
        if num <= n:
            print(num, end=' ')
            num = 2
        else:
            stop = 1
    else:
        i = n