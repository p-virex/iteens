import random

user_name = input('Как вас зовут?\n')

if not user_name:
    print('Вы не представились')
    exit()

print('Привет, {}'.format(user_name))

win_flag = False

while True:
    random_int = random.randint(0, 10)
    for count in range(1, 4):
        user_int = int(input('{}, введите число от 0 до 10\n'.format(user_name)))
        if user_int == random_int:
            print('Вы угадали! Это число: {}'.format(random_int))
            win_flag = True
            break
        print('Вы не угадали, Ваше число: {}, осталось {} попыток'.format(user_int, 3 - count))
    if not win_flag:
        print('{}, вы проиграли! Число было: {}'.format(user_name, random_int))
    else:
        win_flag = False

    user_answer = input('{}, желаете продолжить? N/n - для выхода'.format(user_name))

    if user_answer == 'n':
        break

print('{}, пока!'.format(user_name))
