from functions import shop
from functions import maze
from random import randrange, choice


def game():
    print('1. Магазин       2. Начать игру')
    print('Введите цифру и нажмите enter')
    user_choice = input()
    cnt = 0
    while user_choice not in ['1', '2']:
        if cnt == 5:
            print('>:C')
            cnt = 0
        print('Введите цифру 1 или 2 и нажмите enter')
        user_choice = input()
        cnt += 1
        if user_choice == 'Диалог':
            print('Пасхалка! :)')
    if user_choice == '1':
        shop()
    if user_choice == '2':
        print('Выберите сложность:')
        print('1. Легко     2. Нормально    3. Сложно')
        print('Введите цифру и нажмите enter')
        number = int(input())
        cnt = 0
        while number not in [1, 2, 3]:
            if cnt == 5:
                print('>:C')
                cnt = 0
            print('Введите цифру 1, 2 или 3 и нажмите enter')
            number = int(input())
            cnt += 1
        maze(number)
