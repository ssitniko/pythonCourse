
some_word = input('enter any word in Latin or Cyrillic: ')
print(f'Слово: {some_word}')
print(f'Количество букв: {len(some_word)}')

vowels = 'а', 'у' 'о' 'и' 'ы', 'я', 'ю', 'е', 'ё'
consonants_count = 0
vowels_count  = 0
for i in some_word:
    if i not in vowels:
        consonants_count += 1
    elif i in vowels:
            vowels_count +=1

print(f'Согласных букв: {consonants_count} ')
print(f'Гласных букв:{vowels_count} ')





# while counter <= 50:
#     if counter == 40:
#         break
#     a_word = input('enter any word in Latin or Cyrillic: ')
#     for i in a_word:
#         if type(i) == i.vowels:
#
#
# print(f'количество букв: {count}')


#     print(a_word)
#     count = 0
#     for i in a_word:
#         i = count + 1
#         print(i)


        # temperature = int(temperature)
        # if temperature >= -30 and temperature <= 0:
        #     print('холодно')
        # elif temperature >= 1 and temperature <= 15:
        #     print('прохладно')
        # elif temperature >  = 16 and temperature <= 25:
        #     print('прохладно')
        # elif temperature >= 26 and temperature <= 40:
        #     print('тепло')
        # else:
        #     print(f'несовместима с жизнью температура  {temperature}')
