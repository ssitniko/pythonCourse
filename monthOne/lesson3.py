rounds = 12
while rounds > 0:
    temperature = input('enter temperature: ')
    if temperature == 'exit':
        break
    else:
        temperature = int(temperature)
        if temperature >= -30 and temperature <= 0:
            print('холодно')
        elif temperature >= 1 and temperature <= 15:
            print('прохладно')
        elif temperature >= 16 and temperature <= 25:
            print('прохладно')
        elif temperature >= 26 and temperature <= 40:
            print('тепло')
        else:
            print(f'несовместима с жизнью температура  {temperature}')
        rounds -= 1