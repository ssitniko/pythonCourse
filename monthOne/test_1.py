# def movie_ratings(movie_dict):
#     for k,v in movie_dict.items():
#         if v == {}:
#             print(f'Rating is not yet available for {k}')
#         else:
#             all_ratings = list(v.values())
#             average_rating = sum(all_ratings) // len(all_ratings)
#             print(f'Average rating for {k} is: {average_rating}')


def add_rating(movies_dict, movie_name, name_inp, rate_inp):
    if movie_name not in movies_dict:
        print("This movie doesn't exist!")
    elif name_inp in movies_dict.movie_name.keys():
        print('This name already exist!')
    elif int(rate_inp) not in range(1, 11):
        print('Rate is out of range')
    else:
        movies_dict[movie_name][name_inp] = rate_inp
        print(f'A rating has been added for {movie_name}: {name_inp} rated it {rate_inp}')

test_dict = {
    'detective': {
        'alex': 5,
        'mary': 7,
        'alina': 4
    },
    'serial': {},
    'camedy': {
        'lora': 5,
        'alena': 7,
        'irina': 3
    }
}
movies = dict()

while True:
    movie_input = input('Enter a movie name: ')
    if movie_input == 'q':
        break
    else:
        name_input = input('Enter your name: ')
        rate_input = int(input('Enter your rate: '))
        add_rating(movie_name=movie_input, movies_dict=test_dict, name_inp=name_input, rate_inp=rate_input)
        print(test_dict)

