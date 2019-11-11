import re

print("Лабораторна робота №1 завдання3 \nПанкєєва Софія КМ-93 вар.№15 \nОбчислення конкретної функції, в залежності від введеного значення х.")


def do_input_float(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[-+]?[0-9]{1,}(\.[0-9]{1,}){0,1}$', value)):
            flag = False
            value = float(value)
        else:
            print('error')
    return value


def main():
    x = do_input_float('Введите значение x для решения уравнения ')
    if x > 3.6:
        a = 45 * x ** 2 + 5
        print('Значение x больше 3.6, результат ')
        print(a)
    else:
        a = (5 * x) / (10 * x ** 2 + 1)
        print('Значение меньше или равно 3.6, результат')
        print(a)


main()
