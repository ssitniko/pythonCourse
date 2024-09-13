# # Словари dict, множества - set
# student = {
#    'name': 'azamat',
#     'age': 18
# }
# """add"""
# student['surname'] = 'dairbekov'
# student.update({'weight': 67.4, 'height': 1.777}) # используется при добавлении сразу нескольких,
#
# """edit"""
# student['age'] = 22
#
# """delete"""
# student.pop('weight')  # удаляет и возвращает объект
# del student['height']
# student.clear() # очистка

# print(student)
# # словарь не упорядочен!!!!!
#
# """доступ к значениям словаря"""
# print(student['name'])
# print(student.get('nam', 'нет такого имени'))

# print(student.key())

# for i in student:
#     print(f'{i}: {student[i]}')



from time import sleep

# for i in student:
#     sleep(2)
#     print(f'{}')
#
# for key, value in student.items():
#     print(f'{key} - {value}')

# можно представить данные словаря ввиде столбцов в таблице
"""множество"""

beshbarmak = {"лапша", "мясо", "лук"}
plov = {"мясо", "морковь", "рис"}

print(beshbarmak.difference(plov))
# погуглить работу issubset

# numbers1 = [1, 2, 3, 4, 2, 1, 3, 5]
# numbers2 = (1, 2, 3, 4, 2, 1, 3, 50)
# numbers3 = {1, 2, 3, 4, 2, 1, 3, 5}
# print(type(numbers3))

