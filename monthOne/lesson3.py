""" операторы: принадлежности, назначения, циклы """

""" операторы: назначения """

# number = 5
# number += 5
# number **= 5
# number //= 5
# number -= 5
# print(number)

""" операторы: принадлежности """
# word = 'geeks'
# print('o' in word)
# print('g' in word)
# print('z' not in word)
# print('s' not in word)

""" циклы """
#
# counter = 0
# while counter <=50:
#     if counter == 40:
#         print('stop')
#         break
#     counter +=1
#
#     if counter % 2 == 0:
#         continue
#
#     print('GEEKS', counter)

rounds = 10
while rounds > 0:
    time = input(f'enter time: ({rounds}) ').lower()
    if time == 'quit':
        break
    if time == "утро" or time == 'morning' :
        print("доброе утро")
    elif time == 'день' or time == 'day':
        print("добрый день")
    elif time == 'вечер' or time == 'evening':
        ptint("добрый вечер")
    else:
        print("Здравствуйте! время суток неизвестно")
    rounds -= 1





# rounds = 12
# while rounds > 0:
#     temperature = input('enter temperature: ')
#     if temperature == 'exit':
#         break
#     else:
#         temperature = int(temperature)
#         if temperature >= -30 and temperature <= 0:
#             print('холодно')
#         elif temperature >= 1 and temperature <= 15:
#             print('прохладно')
#         elif temperature >= 16 and temperature <= 25:
#             print('прохладно')
#         elif temperature >= 26 and temperature <= 40:
#             print('тепло')
#         else:
#             print(f'несовместима с жизнью температура  {temperature}')
#         rounds -= 1