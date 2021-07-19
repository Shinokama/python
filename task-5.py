a = float(input("Введите значение выручки: "))
b = float(input("Введите значение издержек: "))
result = a - b
if result > 0:
    print(f'Фирма работает на прибыль.')
    profit = result / a
    e = int(input("Введите численность сотрудников: "))
    re = result / e
    print(f'Рентабельность выручки: {profit:.2f}. Прибыль фирмы в расчете на одного сотрудника: {re:.2f}')
elif result < 0:
    print(f'Фирма работает в убыток.')
elif result == 0:
    print(f'Фирма вышла в 0')
