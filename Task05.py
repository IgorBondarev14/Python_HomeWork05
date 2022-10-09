#Создайте программу для игры в ""Крестики-нолики"".
from random import choice
from tkinter import E

print("\nДля игры необходимо ввести номер сектора, в который вы хотите поставить фигуру")
print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 \n")
move = True
One, Two, Three, Four, Five, Six, Seven, Eight, Nine = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
posssible_move = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Первым ходит Х")
move_count = 9
while move_count > 0:
    if move:
        a = int(input("Введите номер сектора: "))
        while a not in posssible_move:
            a = int(input("Введите номер свободного сектора: "))
        posssible_move.remove(a)
        move_count -= 1
        if a % 2 == 0:
            if a % 4 == 0:
                if a == 4:
                    Four = 'X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Four == Seven or Four == Five == Six:
                        print("Игра окончена")
                        exit()
                    move = not move
                else:
                    Eight = 'X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if Seven == Eight == Nine or Two == Five == Eight:
                        print("Игра окончена")
                        exit()  
                    move = not move  
            else:
                if a == 2:
                    Two = 'X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Two == Three or Two == Five == Eight:
                        print("Игра окончена")
                        exit()  
                    move = not move
                else:
                    Six = 'X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if Three == Six == Nine or Four == Five == Six:
                        print("Игра окончена")
                        exit()
                    move = not move
        else:
            if a % 3 == 0:
                if a == 3:
                    Three = 'X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Two == Three or Three == Six == Nine or Three == Five == Seven:
                        print("Игра окончена")
                        exit()
                    move = not move
                else:
                    Nine = 'X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if Three == Six == Nine or Seven == Eight == Nine or One == Five == Nine:
                        print("Игра окончена")
                        exit()
                    move = not move
            else:
                if a == 1:
                    One = 'X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Two == Three or One == Four == Seven or One == Five == Nine:
                        print("Игра окончена")
                        exit()
                    move = not move
                elif a == 5:
                    Five = 'X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if Four == Five == Six or Two == Five == Eight or One == Five == Nine or Three == Five == Seven:
                        print("Игра окончена")
                        exit()
                    move = not move
                elif a == 7:
                    Seven ='X'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Four == Seven or Seven == Eight == Nine or Three == Five == Seven:
                        print("Игра окончена")
                        exit()
                    move = not move        
    else:
        a = int(input("Введите номер сектора: "))
        while a not in posssible_move:
            a = int(input("Введите номер свободного сектора: "))
        posssible_move.remove(a)
        move_count -= 1
        if a % 2 == 0:
            if a % 4 == 0:
                if a == 4:
                    Four = 'O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Four == Seven or Four == Five == Six:
                        print("Игра окончена")
                        exit()
                    move = not move
                else:
                    Eight = 'O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if Seven == Eight == Nine or Two == Five == Eight:
                        print("Игра окончена")
                        exit()  
                    move = not move  
            else:
                if a == 2:
                    Two = 'O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Two == Three or Two == Five == Eight:
                        print("Игра окончена")
                        exit()  
                    move = not move
                else:
                    Six = 'O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if Three == Six == Nine or Four == Five == Six:
                        print("Игра окончена")
                        exit()
                    move = not move
        else:
            if a % 3 == 0:
                if a == 3:
                    Three = 'O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Two == Three or Three == Six == Nine or Three == Five == Seven:
                        print("Игра окончена")
                        exit()
                    move = not move
                else:
                    Nine = 'O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if Three == Six == Nine or Seven == Eight == Nine or One == Five == Nine:
                        print("Игра окончена")
                        exit()
                    move = not move
            else:
                if a == 1:
                    One = 'O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Two == Three or One == Four == Seven or One == Five == Nine:
                        print("Игра окончена")
                        exit()
                    move = not move
                elif a == 5:
                    Five = 'O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if Four == Five == Six or Two == Five == Eight or One == Five == Nine or Three == Five == Seven:
                        print("Игра окончена")
                        exit()
                    move = not move
                elif a == 7:
                    Seven ='O'
                    print(f" {One} | {Two} | {Three}         1 | 2 | 3\n-----------       -----------\n \
{Four} | {Five} | {Six}         4 | 5 | 6\n-----------       -----------\n\
 {Seven} | {Eight} | {Nine}         7 | 8 | 9\n")
                    if One == Four == Seven or Seven == Eight == Nine or Three == Five == Seven:
                        print("Игра окончена")
                        exit()
                    move = not move
print("Победила 'Дружба'")
