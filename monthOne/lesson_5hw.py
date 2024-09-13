# 1 Создать словарь country_flags: ключом будет домэн страны,
# значениями будут цвета флага страны содержащиеся в множестве,
# например: country_flags = {'kg': {'red', 'yellow'}}
#
# должно быть несколько примеров из любых стран
#
# 2 Создать цикл с вожможностью выхода, в каждом круге которого будет
# запрашиваться цвет у пользователя
#     2.1 У пользователя должна быть возможность ввода одного и более цветов
#     2.2 При вводе одного цвета должны отобразиться все домены стран имеющие этот цвет
#     2.3 При вводе более одного цвета должны отобразиться только домены стран имеющие все указанные цвета
#     2.4 Если введенного цвета нет в заданных флагах, вывести соответствуюещее сообщение на экран и продолжить цикл

country_flags = dict()
country_flags['kg'] = 'red'
country_flags['kz'] = 'blue', 'red'
# country_flags['kg'] = {'red', 'yellow'}
# country_flags['kz'] = {'blue', 'yellow' }
# country_flags['us'] = {'white', 'blue', 'red'}
# country_flags['de'] = {'red', 'black', 'yellow' }
# country_flags['ru'] = {'white', 'blue', 'red'}

print(country_flags)


while True:
    colour_input = input('Введите цвет: ')
    if colour_input == 'q':
        print('program stopped')
        break
    else:
        for k, v in country_flags.items():
            if v == colour_input:
                print(k)
        continue