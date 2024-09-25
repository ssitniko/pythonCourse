
def guess_fun(a_range=0, hint=''):
    a_set = set(range(1,a_range))

    print(a_set)
    guess = len(a_set) // 2 + 1
    a_index = a_set[guess]
    print(guess)
    print(f'Вы загадали число {guess}?')
    hint_inp = input('Введите одну из подсказок: да, больше или меньше: ')
    if hint_inp == 'больше':
        a_set = set(range(a_set))

guess_fun(100)