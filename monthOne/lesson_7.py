
# рассказать про комментарии в python и про тройные ковычки, когда используются?


# lambda_func = lambda n1, n2: n1 + n2
# print(lambda_func(2, 3))
#
# def def_func(n1, n2):
#     return n1 + n2
# print(def_func(2, 3))

# def up_first_letter(word: str)  -> str:
#     return word.title()
#
# def show_words(some_function, some_list):
#     for element in some_list:
#         print(some_function(element))
#
# cities = ['tokmok','bishkek', 'darhan', 'alay']
# show_words(lambda word: word.title(), cities)

# sorted_cities = sorted(cities, key=lambda word: word[1])
# print(sorted_cities)

# filter_cities = list(filter(lambda word: len(word) < 5, cities))
# print(filter_cities)
# map_cities = list(map(lambda word: word.upper(), cities))
# print(map_cities)

# show_words(up_first_letter, cities)
#
# show_words(len, cities)

# try:
#     print(2 * 'abc')
# except:
#     print('Error found!')
# else:
#     print('ok')
# finally:
#     print('checking done')
