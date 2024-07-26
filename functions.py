from random import randrange, choice
from Labirint import game
import eastereggs


class Items:
    def __init__(self):
        price = None
        desc = None
        charges = None


class Cash:

    def __init__(self, money):
        self.money = money

    def purchase(self, other):
        if self.money >= other.money:
            self.money -= other.money
        else:
            print('Недостаточно денег')

    def add(self, amount):
        self.money += amount


wallet = Cash(0)
inventory = []
fail = ['Вы нашли припасы! Но что это? Дверь закрылась! А припасы кажется отравлены...',
        'Боюсь это конец для вас. Вы нашли дракона', 'О нет! Вы нашли древнее зло уничтожающее все на своем пути!']
win = ['Победа! Вы нашли выход!', 'Поздравляю! Вы нашли выход! Ваша награда это свобода!', 'Вы выбрались! Повезло!']
choose1 = 'Выберите один из 2-х путей'
choose2 = 'Выберите один из 3-x путей'
choose3 = 'Выберите один из 4-х путей'


def maze(mode):
    if mode == 1:
        for i in range(5):
            print(choose1)
            print('Введите цифру и нажмите enter')
            user_choice = input()
            cnt = 0
            while user_choice not in ['1', '2']:
                if user_choice == 'cat':
                    print(eastereggs.easter_egg1())
                if cnt == 5:
                    print('>:C')
                    cnt = 0
                print('Введите цифру 1 или 2 и нажмите enter')
                cnt += 1
                user_choice = input()
            if i == 4:
                luck = randrange(100)
                if luck >= 20:
                    print(choice(win))
                    game()
                    wallet.add(1)
                else:
                    print(choice(fail))
                    game()
            else:
                luck = randrange(100)
                if luck > 80:
                    print(choice(win))
                    game()
                    wallet.add(1)
                elif 10 < luck <= 15:
                    print(choice(fail))
                    game()
                elif luck <= 10:
                    wander_shop()
    elif mode == 2:
        for i in range(7):
            print(choose2)
            print('Введите цифру и нажмите enter')
            user_choice = input()
            cnt = 0
            while user_choice not in ['1', '2', '3']:
                #  if user_choice == 'rick':
                #  print(eastereggs.easter_egg2())
                if cnt == 5:
                    print('>:C')
                    cnt = 0
                print('Введите цифру 1, 2 или 3 и нажмите enter')
                cnt += 1
                user_choice = input()
            if i == 6:
                luck = randrange(100)
                if luck >= 35:
                    print(choice(win))
                    game()
                    wallet.add(2)
                else:
                    print(choice(fail))
                    game()
            else:
                luck = randrange(100)
                if luck > 85:
                    print(choice(win))
                    game()
                    wallet.add(2)
                elif 10 < luck <= 20:
                    print(choice(fail))
                    game()

                elif luck <= 10:
                    wander_shop()
    else:
        for i in range(10):
            print(choose3)
            print('Введите цифру и нажмите enter')
            user_choice = input()
            cnt = 0
            while user_choice not in ['1', '2', '3', '4']:
                if user_choice == 'cat':
                    print(eastereggs.easter_egg1())
                if cnt == 5:
                    print('>:C')
                    cnt = 0
                print('Введите цифру 1, 2, 3 или 4 и нажмите enter')
                cnt += 1
                user_choice = input()
            if i == 9:
                luck = randrange(100)
                if luck >= 50:
                    print(choice(win))
                    game()
                    wallet.add(3)
                else:
                    print(choice(fail))
                    game()
            else:
                luck = randrange(100)
                if luck > 95:
                    print(choice(win))
                    game()
                    wallet.add(3)
                elif 10 < luck <= 25:
                    print(choice(fail))
                    game()
                elif luck <= 10:
                    wander_shop()


def shop():
    print('Добро пожаловать в магазин!')
    menu = {'1. Золотое кольцо: Увеличичвает награду за победу на 2$  ', 'Цена: 1$ Действует 3 раунда',
            '2. Талисман: Увеличивает шанс найти зельевара. ', 'Цена: 2$ Действует 2 раунда',
            '3. Тотем: Позволяет возродится 1 раз в любом раунде.', 'Цена: 4$ ',
            '4. Волшебный песок: Позволяет пропустить 1 любой выбор, телепортируя тебя в правильную команту.',
            'Цена: 6$  Кол-во использований: 3 Чтобы использовать вместо цифры напишите "песок"'}
    for i in menu:
        print(i)
    print('Введите цифру и нажмите enter')
    user_choice = input()
    cnt = 0
    while user_choice not in ['1', '2', '3', '4', '5']:
        if user_choice == 'cat':
            print(eastereggs.easter_egg1())
        if cnt == 5:
            print('>:C')
            cnt = 0
        print('Введите цифру 1, 2, 3, 4 или 5 и нажмите enter')
        cnt += 1
        user_choice = input()
    user_choice = int(user_choice)


def wander_shop():
    ...
