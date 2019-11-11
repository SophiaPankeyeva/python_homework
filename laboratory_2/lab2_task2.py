import re
print("Лабораторна робота №2 завдання2 \nПанкєєва Софія КМ-93 вар.№15 \nОбчислити суму, задану формулою.")

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


def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[-+]?[0-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print('error')
    return value


def main():
    x = do_input_float("enter x: ")
    n = do_input_int("enter n: ")

    result = 0
    for i in range(1, n+1):
        result += i / (x**2 + 1)**.5

    print("result: ", round(result, 3))


main()