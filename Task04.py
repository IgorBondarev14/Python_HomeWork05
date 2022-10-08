# #Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?
# Подумайте как наделить бота ""интеллектом""
from random import random, randint, choice

candies = 100
move = bool(choice([True, False]))
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
        if candies > 56:
            taken_candies = 28
            print(taken_candies)
            candies -= taken_candies
            print(f"Осталось {candies} конфет")
            move = not move
        elif candies > 29:
            taken_candies = candies - 29
            print(taken_candies)
            candies -= taken_candies
            print(f"Осталось {candies} конфет")
            move = not move
        elif candies < 29:
            taken_candies = candies
            print(taken_candies)
            candies -= taken_candies
            print(f"Осталось {candies} конфет")
            move = not move    
        else:
            taken_candies = 1
            print(taken_candies)
            candies -= taken_candies
            print(f"Осталось {candies} конфет")
            move = not move
if move: 
    print(f"Победил(а) Бот. {player1}, отдайте все свои конфеты")
else: 
    print(f"Победил(а) {player1}. {player1}, заберите все конфеты, они ваши")