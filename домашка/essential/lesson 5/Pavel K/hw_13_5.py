# Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её отсортированной в порядке возрастания.
a = list(input('Input your text').split())
z = []
for i in a:
    if i.isalpha():
        print(f'мы сортируем цифры {i} - это слово!')
    elif i.isdigit():
        z.append(int(i))
    else:
        f'{i} такое не сортируем'

print(sorted(z))
