mentors = ['Тимур', 'Арсен', 'Гулина', 'Даниель']

while True:
    main_input = input("Введите одну из команд для списка менторов - 'добавить', 'изменить', 'удалить', 'завершить': ")
    if main_input  == 'quit':
        break

    # блок добавить

    if main_input == 'добавить':
        while True:
            add_name = input('Введите имя ментора: ')
            if len(add_name) > 15:
                print('не более 15 символов')
                continue

            elif add_name.title() in mentors:
                print('Такое имя уже есть в списке, введите другое')
                continue

            elif len(mentors) <= 9:
                mentors.append(add_name.title())

            else:
                print('Максимальное количество превышено!')
                break
            print(mentors)
            break

    # блок изменить

    elif main_input == 'изменить':
        while True:
            remove_name = input('Введите имя заменяемого: ')
            remove_name = remove_name.title()
            if len(remove_name) > 15:
                print('не более 15 символов')

            elif remove_name not in mentors:
                print('Такого имени нет в списке')

            else:
                break
        while True:
            new_name = input('Введите новое имя: ')
            if len(new_name) > 15:
                print('не более 15 символов')
                continue
            for i in mentors:
                if i == remove_name:
                   mentors.remove(i)
            mentors.append(new_name.title())
            print(mentors)

            break

    # блок удалить

    elif main_input == 'удалить':
        delete_way = input("Введите способ удаления, 'по имени' или 'по индексу': ")
        if delete_way == 'по имени':
            while True:
                delete_name = input('Введите имя ментора для удаления: ')
                delete_name = delete_name.title()

                if delete_name not in mentors:
                    print('Такого имени нет в списке')
                    continue

                else:
                    for i in mentors:
                        if i == delete_name:
                            mentors.remove(i)
                    break
            print(mentors)
        elif delete_way == 'по индексу':
            while True:
                delete_name = input('Введите имя ментора для удаления: ')
                delete_name = delete_name.title()

                if delete_name not in mentors:
                    print('Такого имени нет в списке')
                    continue

                else:
                    for i in mentors:
                        if i == delete_name:
                            delete_name_index = mentors.index(i)
                            print(delete_name_index)
                            del mentors[delete_name_index]
                    break
            print(mentors)

    elif main_input == 'завершить':
        break

mentors_tuple = tuple(mentors)
print(mentors_tuple)






