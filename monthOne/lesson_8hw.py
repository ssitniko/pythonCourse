# оптимизированный с добавлением функций

def write_in_file(a_file, data, mode='a'):
    with open(a_file, mode) as file:
        file.write(f'\n{data}')


def guess_function(a_list, a_input, a_guess):
    if a_input == 'больше':
        a_list = list(range(a_guess + 1, a_list[-1] + 1))
    elif a_input == 'меньше':
        a_list = list(range(a_list[0], a_guess))

    a_index = len(a_list) // 2
    a_guess = a_list[a_index]
    return a_guess, a_list


while True:
    try:
        main_input = int(input('Можете ввести высшую цифру диапазона(в первоначальной игре введите 100): '))
        if main_input <= 0:
            print('Число должно быть больше 0')
            continue
        print(f"Загадайте целое число от 1 до {main_input}, затем введите одну из трех подсказок: да, больше или меньше ")
        break
    except ValueError:
        print('Вводите только целое число')


guess_list = list(range(1,main_input + 1))
guess = len(guess_list) // 2
count = 0

while True:
    guess_input = input(f'Вы загадали число {guess}?: ')

    if guess_input == 'больше':
        count += 1
        write_in_file('result.txt', guess,)
        guess, guess_list = guess_function(guess_list, guess_input, guess)


    elif guess_input == 'меньше':
        count += 1
        write_in_file('result.txt', guess, )
        guess, guess_list = guess_function(guess_list, guess_input, guess)

    elif guess_input == 'да':
        print('Спасибо за игру!')
        count += 1
        write_in_file('result.txt', f'\nКоличество попыток {count}, \nзагаданное число {guess}')
        break

    else:
        print('Ваш ответ должен быть только: да, больше или меньше')




# Первоначальное решение, сделал самостоятельно, не гуглил (примерно за 2 часа)
#
# print("Загадайте целое число от 1 до 100, затем введите одну из трех подсказок: да, больше или меньше ")
#
# guess_list = list(range(1,101))
# guess = len(guess_list) // 2
# count = 0
#
# while guess_list:
#     guess_input = input(f'Вы загадали число {guess}?: ')
#
#     if guess_input == 'больше':
#         count += 1
#         with open('result.txt', 'a') as result:
#             result.write(f'\n{guess}')
#         guess_list = list(range(guess + 1, guess_list[-1] + 1))
#         guess_index = len(guess_list) // 2
#         guess = guess_list[guess_index]
#
#
#         print(count)
#
#     elif guess_input == 'меньше':
#         count += 1
#         with open('result.txt', 'a') as result:
#             result.write(f'\n{guess}')
#         guess_list = list(range(guess_list[0], guess))
#         guess_index = len(guess_list) // 2
#         guess = guess_list[guess_index]
#         count += 1
#
#
#     elif guess_input == 'да':
#         print('Спасибо за игру!')
#         count += 1
#         with open('result.txt', 'a') as result:
#             result.write(f'\nКоличество попыток {count}, \nзагаданное число {guess}')
#         print(count)
#         break
#
#     else:
#         print('Ваш ответ должен быть только: да, больше или меньше')
#
#




