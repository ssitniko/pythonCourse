# calculating weekly expenses program

monday = int(input('введите расход ПН: '))
tuesday = int(input('введите расход ВТ: '))
wednesday = int(input('введите расход СР: '))
thursday = int(input('введите расход ЧТ: '))
friday = int(input('введите расход ПТ: '))
saturday = int(input('введите расход СБ: '))
sunday = int(input('введите расход ВС: '))

total_expenses_amount = monday + tuesday + wednesday + thursday + friday + saturday + sunday

average_expenses_amount = total_expenses_amount / 7

print(f'Cредняя сумма расходов за день: {round(average_expenses_amount, 1)}')