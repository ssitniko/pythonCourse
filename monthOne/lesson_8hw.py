

# Первоначальное решение, сделал самостоятельно, даже не гуглил (примерно за 2 часа)

print("Загадайте целое число от 1 до 100, затем введите одну из трех подсказок: да, больше или меньше ")

guess_list = list(range(1,101))
guess = len(guess_list) // 2
count = 0

while guess_list:
    guess_input = input(f'Вы загадали число {guess}?: ')

    if guess_input == 'больше':
        count += 1
        with open('result.txt', 'a') as result:
            result.write(f'\n{guess}')
        guess_list = list(range(guess + 1, guess_list[-1] + 1))
        guess_index = len(guess_list) // 2
        guess = guess_list[guess_index]


        print(count)

    elif guess_input == 'меньше':
        count += 1
        with open('result.txt', 'a') as result:
            result.write(f'\n{guess}')
        guess_list = list(range(guess_list[0], guess))
        guess_index = len(guess_list) // 2
        guess = guess_list[guess_index]
        count += 1


    elif guess_input == 'да':
        print('Спасибо за игру!')
        count += 1
        with open('result.txt', 'a') as result:
            result.write(f'\nКоличество попыток {count}, \nзагаданное число {guess}')
        print(count)
        break

    else:
        print('Ваш ответ должен быть только: да, больше или меньше')






