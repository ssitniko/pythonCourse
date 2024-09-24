# контекстный менеджер with, работа с файлами
# w - write (запись, перезапись)
# a - add (дозапись)
# x - (создает уникальный файл)

# file = open('new_file.txt', 'w')
# file.write('текст на кириллице')
# file.close()

# with open('new_file.txt', 'a') as new_file:
#     new_file.write('\nвторая строка')
#
with open('new_file.txt', 'a') as file:
     file.write('новый файл')
     print(file)

# with open('new_file.txt', 'r') as file:
#     print(file.read())

# from time import sleep
#
# with open('new_file.txt', 'r') as file:
#     for i in file.read():
#         sleep(1)
#         print(i, end='')

# file.readline() # игнорирует первую строку
# print(file.readlines()) # разбивает на строки
# print(file.read()) # читает все в одну строку

# a_list = ['hello', 'good morning', 'good afternoon', 'good evening']
#
# for i in a_list:
#     print(i, end='')

