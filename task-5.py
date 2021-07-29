"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def summa(my_list=None):
    """
    Введите последовательность чисел, разделенных пробелом.
    Для остановки укажите ! в качестве аргумента (можно в составе списка, тогда остановка произойдет при первой встрече
    аргумента)
    :param my_list: последовательность чисел, разделенных пробелом
    :return: возвращает окончательный результат сложения
    """
    if_continue = True
    result = 0.0
    while if_continue is True:
        if my_list is None:
            my_list = input(f'Введите последовательность чисел, разделенных пробелом. Для остановки укажите ! '
                            f'вместо любого аргумента. Данные, не являющиеся числами, будут игнорироваться.\n')
        my_list = my_list.split()
        for el in my_list:
            if el == "!":
                if_continue = False
            else:
                try:
                    el = float(el)
                except ValueError:
                    continue
                else:
                    result += el
        if if_continue is True:
            print(f'Результат сложения равен {result:g}. Продолжите ввод данных.\n')
            my_list = None
    print(f'Вычисление завершено, окончательная сумма равна {result:g}')
    return result


if __name__ == "__main__":
    summa()
