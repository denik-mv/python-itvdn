# Задание 1
# Создайте функцию от произвольного количества аргументов, которая вычисляет среднее
# арифметическое данных чисел. Вычислите при помощи неё среднее арифметическое двух заданных
# чисел и среднее арифметическое чисел из заданного диапазона.

l = [1, 3, 2, 5 , 9 ,8, 3, 5, 6]

def s(*args):
    x = sum(*args) / len(*args)
    return int(x)

print(f'{s(l)}\n{s(l[3:5])}')
