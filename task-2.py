"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(a, b):
    try:
        if b == 0:
            raise ZeroError("Делить на 0 нельзя")
    except ZeroError as ze:
        print(ze)
    else:
        result = a / b
        return result


# Проверки
print(div(1, 0))
print(div(0, 1))
print(div(10, 5))
