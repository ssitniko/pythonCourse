
num_list = [25, 50, 75, 1500, 3000]

def nearest_number(numbers, target: int):
    """принимает лист или кортеж, целевое число и возвращает ближайшее к цел.ч."""
    result = list()
    dict_num = dict()
    for num in numbers:
        if num < target:
            dif_num = target - num
            dict_num[num] = dif_num
        elif num > target:
            dif_num = num - target
            dict_num[num] = dif_num
    temp_dict = dict_num.copy()
    while temp_dict:
        min_key = min(temp_dict, key=temp_dict.get)
        result.append(min_key)
        del temp_dict[min_key]
    final = (target, result,)
    print(final)

nearest_number(num_list, 10)



# 2. примеры использования lambda функции с map() и filter()

# a_list = list(range(1,20))
# print(a_list)
#
# map_list = list(map(lambda i: i ** 3, a_list))
# print(map_list)
#
#
# season_list = ['winter', 'Summer', 'autumn', 'Spring']
# filtered_list_1 = list(filter(lambda i: i.istitle(), season_list))
# print(filtered_list_1)


# 3  
# def get_element(iterable, index):
#     return iterable[index]
#
# a_list = [1, 4, 6, 3, 'hello', ['name']]
# print(a_list)
#
#
# while True:
#     try:
#         input_index = input("Enter index to get element, otherwise enter quit: " )
#     except Exception as e:
#         print(e)
#
#
#     if input_index != 'quit':
#         try:
#             input_index = int(input_index)
#         except Exception as e:
#             print(e)
#         try:
#             print(get_element(a_list, input_index))
#         except:
#             print('Enter index in range of 0-5')
#
#
#     elif input_index == 'quit':
#         print('Program finished')
#         break