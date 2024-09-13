# calculating weekly expenses program
days = []
expenses = []

count = 7
while count > 0:
    exp_input = int(input('введите по очередно расходы за 7 дней недели: '))
    expenses.append(exp_input)
    count -= 1
    if count == 0:
        break
total_exp = sum(expenses) / 2
print(f'Средняя сумма расхода {total_exp}')









# monday = int(input('введите расход ПН: '))
# tuesday = int(input('введите расход ВТ: '))
# wednesday = int(input('введите расход СР: '))
# thursday = int(input('введите расход ЧТ: '))
# friday = int(input('введите расход ПТ: '))
# saturday = int(input('введите расход СБ: '))
# sunday = int(input('введите расход ВС: '))
#
# total_expenses_amount = (monday + tuesday + wednesday +
#                          thursday + friday + saturday + sunday)
#
# average_expenses_amount = total_expenses_amount / 7
#
# print(f'Cредняя сумма расходов за день: {round(average_expenses_amount, 1)}')