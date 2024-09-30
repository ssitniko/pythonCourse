from monthOne.lesson_6hw import name_input

movies = dict()
ratings = dict()
find = True


def add_movie(add_inp, movies_dict):
    if add_inp in movies_dict:
        print('This movie already exist!')
    else:
        movies_dict[add_inp] = dict()

def add_rating(movie_name, movies_dict,):
    if movie_name not in movies_dict:
        print("This movie doesn't exist!")
    else:
        while True:
            name_input = input('Enter your name: ')
            if name_input in movies.values():


            rate_input = input('Enter your rate: ')
            if rate_input not in range(1, 11):
                print('This name already exist, enter another name')
            movies_dict[movie_name][name_input] = rate_input
            print(f'A rating has been added for {movie_name}: {name_input} rated it {rate_input}')

def get_movie_ratings(movie_dict):
    for k,v in movie_dict.items():
        if v == {}:
            print(f'Rating is not yet available for {k}')
        else:
            all_ratings = list(v.values())
            average_rating = sum(all_ratings) // len(all_ratings)
            print(f'Average rating for {k} is: {average_rating}')

test_dict = {
    'detective': {
        'alex': 5,
        'mary': 7,
        'alina': 4
    },
    'serial': {}
}
movie_ratings(test_dict)


# while True:
#     movies_input = input('Введите название фильма: ').title()
#     if movies_input == 'q':
#         break
#     add_movie(movies_input, movies)
#     print(f'{movies_input} has been added successfully!')
#     print(movies)
#
#     a_movies_input = input('Введите название фильма: ').title()
#     add_rating(a_movies_input, movies)
#     print(movies)




# =========================================================
# while True:
#     if find:
#         while True:
#             movies_input = input('Введите название фильма: ').title()
#             if movies_input in movies:
#                 print('This movie already exists!')
#                 continue
#             else:
#                 break

    #     while True:
    #         name_input = input('Введите ваше имя: ').title()
    #         name_find = False
    #         for k, v in movies.items():
    #             if name_input in v:
    #                 print('This name already exists')
    #                 name_find = True
    #
    #         if not name_find:
    #             break
    #
    #     while True:
    #         rating_input = int(input('Введите оценку в диапазоне от 1 до 10: '))
    #         if rating_input not in range(11):
    #             print('Оценка не в диапазоне от 1 до 10!')
    #             continue
    #         else:
    #             break
    #
    # movie_rating(movies_input, name_input, rating_input)
    # print('Movie added successfully')
    #
    # # movies[movies_input] = dict()
    # # movies[movies_input][name_input] = rating_input
    # print(f'A rating has been added for {movies_input}: {name_input} rated it {rating_input}')
    # print(movies)

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

