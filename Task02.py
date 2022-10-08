# #Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять 
# первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import random


player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
candies = 2021
move = bool(random)
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