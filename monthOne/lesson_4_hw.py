mentors = ['Тимур', 'Арсен', 'Гулина', 'Даниель']

while True:
    add_name = input('Введите имя ментора: ')
    if len(add_name) > 15:
        print('не более 15 символов')

    elif add_name.title() in mentors:
        print('Такое имя уже есть в списке, введите другое')

    elif len(mentors) <= 9:
        mentors.append(add_name.title())

    else:
        print('Максимальное количество превышено!')
        break

    print(mentors)

# while True:
#     add_remove_name = input('Введите имя заменяемого: ')
#     if len(add_remove_name) > 15:
#
#     if add_remove_name.title() not in mentors:
#         print('Такого имени нет в списке')
#
#     add_new_name = input('Введите новое имя: ')





