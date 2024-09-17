
movies = dict()
ratings = dict()

def movie_rating (movie, name, rating ):
    movies[movie] = ratings
    movies[movie][name] = rating
    return movies

while True:
    movies_input = input('Введите название фильма: ').title()
    if movies_input in movies:
        print('This movie already exists!')
    name_input = input('Введите ваше имя: ').title()

    if name_input:
        for k, v in movies.items():
            if name_input in v:
                print('This name already exists, please enter another name')
            continue

    rating_input = input('Введите оценку в диапазоне от 1 до 10: ')
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