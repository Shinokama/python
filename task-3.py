n = int(input("Введите любое целое число: "))
n = n + int(str(f'{n}{n}')) + int(str(f'{n}{n}{n}'))
print(f'Спасибо, вот сумма в формате "n + nn + nnn", где "n" - ваше число: {n}')
