"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    """
    Укажите 3 любых числа в качестве аргументов. Функция возвращает сумму наибольших двух аргументов
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print("вводите только числа")
    else:
        my_list = [a, b, c]
        my_list.sort(reverse=True)
        my_sum = my_list[0] + my_list[1]
        print(f'Сумма двух наибольших аргументов: {my_sum:g}')
        return my_sum


if __name__ == "__main__":
    my_func(1, 5, 7)
