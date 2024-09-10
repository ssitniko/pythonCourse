# списки, кортежи, индексы и срезы, Встроенные функции к наборам элементов, списковое включение
# List comprehension.

students = ['bilal', 'dair', 'aidana', 'ulan']
print(students)
"""индексы"""
# print(students[0])
# print(students[2])
# print(students[-1])
# print(students[-2])
#
# """срезы [start:stop:step"""
# print(students[1:3:1])
# print(students[:2])
# print(students[::2])

"""add"""
# students.append('sergei') # добавляет один объект в конец списка
# students.insert(2, 'ali') # добавляет один объ. в опр. место
# students.insert('marat', 'kamila') # добавляет  много объ. в конец

# """edit"""
# students.sort()
# students.reverse()
# students[0] = 'abdel'
#
# """delete"""
# students.remove()
# deleted = students.pop(-1)
# del students[:2]
# students.clear()

numbers = (34, 67, 12, 46, 59, 87, 92)
# из одного объекта не получится
""" встроенные функции """
numbers = [23, 45, 67, 89, 90, 11]
print(len(numbers)) # возврашает количество объектов
print(min(numbers))
print(max(numbers))
print(any(numbers)) #
print(all(numbers))

count = 0
for i in numbers:
    count += 1
print(count)

# доп. домашка
реализовать функции min, max, sum

rus = 'абв'
eng = 'abs'
print(rus[0])
print(rus[eng.index('a')])







