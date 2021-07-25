"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо
использовать функцию input().
"""

my_list = []
num = input("Введите количество элементов: ")
try:
    num = int(num)
    for n in range(0, num):
        element = input(f'Введите {n + 1}-й элемент: ')
        my_list.append(element)
    print(f'Ваш список до перестановки:\n{my_list}')
    le = len(my_list)
    ind1 = 0
    ind2 = ind1 + 1
    while ind1 < le and ind2 < le:
        my_list[ind1], my_list[ind2] = my_list[ind2], my_list[ind1]
        ind1 += 2
        ind2 += 2
    print(f'Ваш список после перестановки:\n{my_list}')
except ValueError:
    print("Количество должно быть цифрой")
