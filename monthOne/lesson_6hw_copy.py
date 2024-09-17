from operator import contains

movies = dict()
ratings = dict()
find = True

def movie_rating (movie, name, rating ):
    movies[movie] = ratings
    movies[movie][name] = rating
    return movies

while True:
    if find:
        while True:
            movies_input = input('Введите название фильма: ').title()
            if movies_input in movies:
                print('This movie already exists!')
                continue
            else:
                break

    # name_input = input('Введите ваше имя: ').title()
        while True:
            name_input = input('Введите ваше имя: ').title()
            name_find = False
            for k, v in movies.items():
                if name_input in v:
                    print('This name already exists')
                    name_find = True

            if not name_find:
                break

        while True:
            rating_input = int(input('Введите оценку в диапазоне от 1 до 10: '))
            if rating_input not in range(11):
                print('Оценка не в диапазоне от 1 до 10!')
                continue
            else:
                break

    movie_rating(movies_input, name_input, rating_input)
    print('Movie added successfully')

    # movies[movies_input] = dict()
    # movies[movies_input][name_input] = rating_input
    print(f'A rating has been added for {movies_input}: {name_input} rated it {rating_input}')
    print(movies)





# for movie in movies:
    #     if movies_input in movies:
    #         print('Такой фильм уже есть')
    #     else:
    #         movies[movies_input] = {'rating': 10}
    #     print(movies)