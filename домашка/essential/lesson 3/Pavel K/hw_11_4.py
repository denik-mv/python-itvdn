# Опишите свой класс исключения. Напишите функцию, которая будет выбрасывать данное исключение, если пользователь
# введёт определённое значение, и перехватите это исключение при вызове функции.

class MyError(Exception):
    def __init__(self,mye):
        self.mye = mye

a = input('Введите число больше равно 100 и меньше равно 300')

try:
    a = int(a)
    if a < 100:
        raise MyError (f'{a} меньше 100!')
    if a > 300:
        raise MyError (f'Ну куда ты так разогнался, {a} больше чем 300!')
except ValueError:
    print(f'{a} - это вообще строка, просили число, число!')
except MyError as me:
    print(me)
else:
    print(a,'Ты справился!')
