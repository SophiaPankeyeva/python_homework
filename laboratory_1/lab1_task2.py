import re

print("Лабораторна робота №1 завдання2 \nПанкєєва Софія КМ-93 вар.№15 \nНаписати програму, яка аналізує дані про вік і відносить людину до однієї з чотирьох груп: дошкільник, учень, працівник, пенсіонер. \nВік вводиться з клавіатури.")


def do_input(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print('error')
    return value


def main():
    age = do_input('введіть потрібний вам вік age= ')
    if (age >= 0) and (age < 6):
        print('дошкільник')
    elif (6 <= age) and (age < 23):
        print('учень')
    elif (23 <= age) and (age < 60):
        print('працівник')
    elif (age >= 60) and (age <= 100):
        print('пенсіонер')
    elif age < 0:
        print('ви ще не народились, введіть інше значення')
    elif age > 100:
        print('думаю, ви вже померли. введіть інше значення ')


main()
