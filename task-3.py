"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict.
"""

month = input("Введите числовой номер месяца: ")
try:
    month = int(month)
    # решение через list
    if month in [12, 1, 2]:
        print("Зима (решено через list)")
    elif month in [3, 4, 5]:
        print("Весна (решено через list)")
    elif month in [6, 7, 8]:
        print("Лето (решено через list)")
    elif month in [9, 10, 11]:
        print("Осень (решено через list)")
    else:
        print("Это не номер месяца (решено через list)")

    # решение через dict
    seasons = {"Зима": (12, 1, 2), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}
    check = False
    for season, months in seasons.items():
        if month in months:
            check = True
            print(f'{season} (решено через dict)')
    if not check:
        print("Это не номер месяца (решено через dict)")
except ValueError:
    print("Номер месяца должен быть цифрой")
