

while True:
    message = input('enter any word in Latin or Cyrillic: ')
    if message == 'quit':
        break
    letter_quantity = len(message)
    print(f'Слово: {message}')
    print(f'Количество букв: {letter_quantity}')

    vowels_latin = 'a e i o u y'
    vowels_cyrilic = 'а у о и ы я ю е ё'

    cyrillic = 'а б в г д е ё ж и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'
    latin = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'


    consonants_count_c = 0
    vowels_count_c  = 0

    consonants_count_l = 0
    vowels_count_l = 0

    if message in cyrillic:
        for item_c in message:
            if item_c not in vowels_cyrilic:
                consonants_count_c += 1
            else:
                vowels_count_c +=1

        percentage_consonants_c = round((consonants_count_c / letter_quantity * 100), 2)
        percentage_vowels_c = round((vowels_count_c / letter_quantity * 100), 2)

        print(f'Согласных букв: {consonants_count_c} ')
        print(f'Гласных букв:{vowels_count_c} ')
        print(f'Гласные/Согласные {percentage_vowels_c}/{percentage_consonants_c}')

    else:
        for item_l in message:
            if item_l not in vowels_latin:
                consonants_count_l += 1
            else:
                vowels_count_l +=1

        percentage_consonants_l = round((consonants_count_l / letter_quantity * 100), 2)
        percentage_vowels_l = round((vowels_count_l / letter_quantity * 100), 2)

        print(f'Согласных букв: {consonants_count_l} ')
        print(f'Гласных букв:{vowels_count_l} ')
        print(f'Гласные/Согласные {percentage_vowels_l}/{percentage_consonants_l}')








