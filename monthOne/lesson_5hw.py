# country flags colours program

country_flags = dict()

country_flags['kg'] = {'red', 'yellow'}
country_flags['kz'] = {'blue', 'yellow' }
country_flags['us'] = {'white', 'blue', 'red'}
country_flags['de'] = {'red', 'black', 'yellow' }
country_flags['ru'] = {'white', 'blue', 'red'}

print(country_flags)


user_input = ''
while user_input != 'q':
    user_input = (input('Введите цвета через запятую: '))
    user_input_1 = user_input.split(',')
    user_colors = set(color.strip().lower() for color in user_input_1)

    at_least_one_flag = False

    for k, v in country_flags.items():
        if user_colors.issubset(v):
            print(k)
            at_least_one_flag = True

    if not at_least_one_flag:
        print('Вы ввели цвета которых нет, введите другой цвет')









# код работает но только с одним цветом
# while True:
#     colour_input = input('Введите цвет: ')
#     if colour_input == 'q':
#         print('program stopped')
#         break
#     for k,v in country_flags.items():
#         if colour_input in v:
#             print(k)




