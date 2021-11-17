contr = int(input('Ваша сумма вклада: '))
sum = 0
counter = 0
while counter != 5:
    sum = contr / 100 * 10
    contr += sum
    counter += 1
print(f'Общая сумма на счету пользователя составит: {round(contr, 1)} р. + Бонус {120 * counter} р.\nИтог: {round(contr, 1) + 120 * counter} р.')
