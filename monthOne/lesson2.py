# Логический тип данных, Операторы: условные, сравнения, логические

# print(type)
#
# time = input('enter time: ').lower()
#
# if time == "утро" or time == 'morning' :
#     print("доброе утро")
# elif time == 'день' or time == 'day':
#     print("добрый день")
# elif time == 'вечер' or time == 'evening':
#     ptint("добрый вечер")
# else:
#     print("Здравствуйте! время суток неизвестно")

""" Логические сравнения"""
# and or not
# print(2 > 3 or 2 < 3)
# print(2 > 3 and 2 < 3)
# print(not False)
# print(not True)


"""Oператоры сравнения"""

# print(2 == 3)
# print(2 != 3)
# print(2 > 3)
# print(2 < 3)
# print(2 >= 3)
# print(2 <= 3)
# print(2 == 3)
# print(2 < 3)
# print(2 <= 3)

# calculating weekly expenses program

# monday = int(input('введите расход ПН: '))
# tuesday = int(input('введите расход ВТ: '))
# wednesday = int(input('введите расход СР: '))
# thursday = int(input('введите расход ЧТ: '))
# friday = int(input('введите расход ПТ: '))
# saturday = int(input('введите расход СБ: '))
# sunday = int(input('введите расход ВС: '))
#
# total_expenses_amount = (monday + tuesday + wednesday +
#                          thursday + friday + saturday + sunday)
#
# average_expenses_amount = total_expenses_amount / 7
#
# if average_expenses_amount >= 1 and  average_expenses_amount < 100:
#     print('мало потрачено')
# elif average_expenses_amount >= 101 and  average_expenses_amount < 500:
#     print('средне потрачено')
#
# elif average_expenses_amount >= 501:
#     print("много потрачено")
# else:
#     print('ничего не потрачено')
#
# print(f'Cредняя сумма расходов за день: {round(average_expenses_amount, 1)}')



temperature = int(input('enter temperature: '))

if temperature >= -30 and temperature <= 0:
    print('холодно')
elif temperature >= 1 and temperature <= 15:
    print('прохладно')
elif temperature >= 16 and temperature <= 25:
    print('прохладно')
elif temperature >= 26 and temperature <= 40:
    print('тепло')
else:
    print(f'несовместима с жизнью температура  {temperature}')