# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

from itertools import count


data_in = open('in.txt','w')
data_in.write('abbccc222222dddd/////eeee')
data_in.close()

data_in = open('in.txt', 'r')
text = str(*data_in)
data_in.close()
print(f"Так выглядит исходный текст: {text}")

encoded_text = ''
count = 1
for i in range(0, len(text) - 1):
    if text[i] == text[i + 1]:
        if i == len(text) - 2:
            count += 1
            encoded_text = encoded_text + str(count) + '*' + text[i] + ' '
            break
        count += 1
    else:
        encoded_text = encoded_text + str(count) + '*' + text[i] + ' '
        count = 1
print(f"Так выглядит сжатый текст: {encoded_text}")

data_out = open('out.txt', 'w')
data_out.write(encoded_text)
data_out.close()

data_decoded = open('out.txt', 'r')
new_text = str(*data_decoded)
data_decoded.close()
decoded_text = ''
for i in range(1, len(new_text) - 1):
    if new_text[i] == '*':
        decoded_text = decoded_text + int(new_text[i - 1]) * str(new_text[i + 1])
print(f"Так выглядит разархивированный текст: {decoded_text}")
