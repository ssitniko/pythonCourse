

movies = dict()
ratings = dict()
a_list = list()

def enter_movie(a_movie):
    movies[a_movie] = ratings

    print('Movie added successfully')
    return movies

def enter_name_rating(a_name, a_rating):
    for k2, v2 in movies.items():
        if a_name in v2:
            print('This name already exists')

        else:
            v2[a_name] = a_rating
            print(f'A rating has been added: {a_name} rated it {a_rating}')
            break

while True:
    main_input = input('Введить одну из команд: добавить фильм, добавить рейтинг, просмотреть рейтинг: ')

    if main_input == 'добавить фильм':
        while True:
            movie_input = input('Enter the name of a movie: ').title()
            if movie_input in movies:
                print('This movie already exists!')
                continue
            else:
                enter_movie(movie_input)
                print(movies)
                break
    elif main_input == 'добавить рейтинг':
        while True:
            name_input = input('Введите ваше имя: ').title()
            rating_input = int(input('Введите оценку в диапазоне от 1 до 10: '))
            enter_name_rating(name_input, rating_input)
            break

    elif main_input == 'просмотреть рейтинг':
                for k,v in movies.items():
                    for a,b in v.items():
                        a_list.append(b)
                        print((sum(a_list) / len(a_list)))

                        break
                    break

                                        # elif main_input == 'просмотреть рейтинг':
                                        #     while True:
                                        #         rat_input = input('Enter the name of a movie: ').title()
                                        #         if rat_input in movies:
                                        #             for k,v in movies.items():
                                        #                 if rat_input == k:
                                        #                     for a,b in v.items():
                                        #                         a_list.append(b)
                                        #                     print((sum(a_list) / len(a_list)))


                                         #       else:
                                          #          print('This movie is non in archive')
                                           #         continue
    elif main_input == 'q':
        break


# Ниже приведен первоначальный код, только с одной функцией

# movies = dict()
# ratings = dict()
# find = True
#
# def movie_rating (movie, name, rating ):
#     movies[movie] = ratings
#     movies[movie][name] = rating
#     return movies
#
# while True:
#     if find:
#         while True:
#             movies_input = input('Введите название фильма: ').title()
#             if movies_input in movies:
#                 print('This movie already exists!')
#                 continue
#             else:
#                 break
#
#         while True:
#             name_input = input('Введите ваше имя: ').title()
#             name_find = False
#             for k, v in movies.items():
#                 if name_input in v:
#                     print('This name already exists')
#                     name_find = True
#
#             if not name_find:
#                 break
#
#         while True:
#             rating_input = int(input('Введите оценку в диапазоне от 1 до 10: '))
#             if rating_input not in range(11):
#                 print('Оценка не в диапазоне от 1 до 10!')
#                 continue
#             else:
#                 break
#
#     movie_rating(movies_input, name_input, rating_input)
#     print('Movie added successfully')
#
#     # movies[movies_input] = dict()
#     # movies[movies_input][name_input] = rating_input
#     print(f'A rating has been added for {movies_input}: {name_input} rated it {rating_input}')
#     print(movies)





