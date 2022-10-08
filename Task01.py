# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст для проверки:\n").split()
length = len(text)
for i in range(length - 1, 0, -1):
    if text[i].find('абв') != -1:
        text.pop(i)
print(' '.join(text))