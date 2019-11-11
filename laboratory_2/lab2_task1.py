import re

print("Лабораторна робота №2 завдання1 \nПанкєєва Софія КМ-93 вар.№15 \nДано ціле число N(>0). \nНеобхідно знайти подвійний факторіал N: N!!= N•(N-2) •(N-4)• ... \n(останній співмножник дорівнює 2, якщо N - парне, і 1, якщо N - непарне). \nЩоб уникнути цілочисельного переповнення, обчислювати цей добуток за допомогою дійсної змінної і вивести його як дійсне число.")

def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print('error')
    return value


def double_factorial(n):
    if n == 2:
        return n
    if n == 1:
        return n
    return n * double_factorial(n - 2)


n = do_input_int(" Input n: ")
n = double_factorial(n)
print(n)

