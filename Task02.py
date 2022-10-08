# #Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
from random import random, randint, choice
print("Выберите вариант игры:\n1. Друг против друга\n2. Против бота")
variant = int(input("Ваш выбор - "))
while variant != 1 and variant != 2:
    print("Введите 1 или 2")
    variant = int(input())
candies = 2021
move = bool(choice([True, False]))
if variant == 1:
    player1 = input('Введите имя первого игрока: ')
    player2 = input('Введите имя второго игрока: ')
    while candies > 0:
        if move:
            print(f"Введите количество конфет, которые берет {player1} - ")
            taken_candies = int(input())
            while taken_candies > 28:
                print(f"Вы не можете взять больше, чем 28 конфет.\n \
                Введите количество конфет, которые берет {player1} - ")
                taken_candies = int(input())
            if candies > taken_candies:
                candies -= taken_candies
                print(f"Осталось {candies} конфет")
                move = not move
            else:
                while taken_candies > candies:
                    print(f"Вы не можете взять конфет больше, чем осталось ({candies}).\n \
                    Введите количество конфет, которые берет {player1} - ")
                    taken_candies = int(input())
                candies -= taken_candies
                print(f"Осталось {candies} конфет")
                move = not move
        else:
            print(f"Введите количество конфет, которые берет {player2} - ")
            taken_candies = int(input())
            while taken_candies > 28:
                print(f"Вы не можете взять больше, чем 28 конфет.\n \
                Введите количество конфет, которые берет {player2} - ")
                taken_candies = int(input())
            if candies > taken_candies:
                candies -= taken_candies
                print(f"Осталось {candies} конфет")
                move = not move
            else:
                while taken_candies > candies:
                    print(f"Вы не можете взять конфет больше, чем осталось ({candies}).\n \
                    Введите количество конфет, которые берет {player2} - ")
                    taken_candies = int(input())
                candies -= taken_candies
                print(f"Осталось {candies} конфет")
                move = not move
    if move: 
        print(f"Победил(а) {player2}. {player1}, отдайте все свои конфеты оппоненту")
    else: 
        print(f"Победил(а) {player1}. {player2}, отдайте все свои конфеты оппоненту")
else:
    player1 = input('Введите имя игрока: ')
    while candies > 0:
        if move:
            print(f"Введите количество конфет, которые берет {player1} - ")
            taken_candies = int(input())
            while taken_candies > 28:
                print(f"Вы не можете взять больше, чем 28 конфет.\n \
                Введите количество конфет, которые берет {player1} - ")
                taken_candies = int(input())
            if candies > taken_candies:
                candies -= taken_candies
                print(f"Осталось {candies} конфет")
                move = not move
            else:
                while taken_candies > candies:
                    print(f"Вы не можете взять конфет больше, чем осталось ({candies}).\n \
                    Введите количество конфет, которые берет {player1} - ")
                    taken_candies = int(input())
                candies -= taken_candies
                print(f"Осталось {candies} конфет")
                move = not move
        else:
            print("Количество конфет, которые берет Бот - ")
            if candies > 28:
                taken_candies = randint(1, 29)
                print(taken_candies)
                candies -= taken_candies
                print(f"Осталось {candies} конфет")
                move = not move
            else:
                taken_candies = randint(1, candies + 1)
                print(taken_candies)
                candies -= taken_candies
                print(f"Осталось {candies} конфет")
                move = not move
    if move: 
        print(f"Победил(а) Бот. {player1}, отдайте все свои конфеты")
    else: 
        print(f"Победил(а) {player1}. {player1}, заберите все конфеты, они ваши")