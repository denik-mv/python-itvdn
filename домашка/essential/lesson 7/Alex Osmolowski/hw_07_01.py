# Задание 1
# Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
# чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый
# интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При
# замене последнего на другой, взаимодействующий с пользователем иным способом, программа
# должна продолжать корректно работать.

import pprint
import sys
import os


# pprint.pprint(dir(os))
# print(os.getcwd())
# sys.path.insert(0, os.getcwd())
# print(sys.path[0])


import mylinks


def main():
    links = {}
    f = {"1": add_link_to, "2": get_link_from}

    while True:
        print('1. Добавить ссылку')
        print('2. Показать ссылку')
        print('3. Выход')

        choice = input('> ').strip()
        if choice == "3":
            break
        try:
            f[choice](links)
        except KeyError:
            print('Некорректный ввод пункта меню')
        print()


if __name__ == '__main__':
    main()