#функции, аргументы, параметры, виды аргументов



# def sum_up(*args):  # !!!! ЗАПАКОВЫВАЕТ АРГУМЕНТЫ В КОРТЕЖ
#     return sum(args)
#
# print(sum_up(2, 4, 5, 6, 6, 3))
#
# def menu(**kwargs):   # !!! ВОЗВРАЩАЕТ СЛОВАРЬ
#     return kwargs
#
# monday = menu(eat='burger', drink='coffe', desert='ice cream')
# print(monday)

def get_hidden_card(num, open_num=4):
    list_num = list(num)
    list_num1 = list_num[:12]
    print(list_num1)

input_num = int(input('Введите номер кредитной карты: '))
get_hidden_card(input_num)











# def get_data(name, surname='неуказано'):
#     print(f'name: {name} surname: {surname}')
#
# get_data(surname='sitnikov', name='sergei')
#
#
# def len1(iterable):
#     counter = 0
#     for i in iterable:
#         counter += 1
#     return counter
#
# letters_count = len1('geeks')
# print(letters_count)
#
# length = 8
# width = 4
# square = length * width
#
# def get_square(length, width):
#     """вычисляет площадь"""
#     square = length * width
#     return square
#
# print(get_square(length, width))
# print(get_square.__doc__)