import math
import re

print("Лабораторна робота №1 завдання1 \nПанкєєва Софія КМ-93 вар.№15 \nПотрібно обчислити, скільки банок фарби потрібно, щоб пофарбувати поверхню циліндричної форми. \nПофарбувати треба і зовні, і зсередини. \nКористувач вводить діаметр і висоту бака, а також, яку площу можна забарвити однією банкою фарби.")

def do_input_float(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}(\.[0-9]{1,}){0,1}$', value)):
            flag = False
            value = float(value)
        else:
            print('error')
    return value


diametr = do_input_float("Введіть діаметр бака: ")
height = do_input_float("введіть висоту бака: ")
area = do_input_float("введіть площу, яку можна пофарбувати: ")

N=math.ceil((math.pi*diametr*height+math.pi*diametr**2/2)/area)
print(N)
