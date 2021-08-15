"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

import re
from datetime import date as d


def date_format(date):
    try:
        if re.match("^\d\d-\d\d-\d\d\d\d$", date):
            return date
        else:
            raise ValueError("Некорректный формат данных. Ожидается дата в следующем виде: 'ДД-ММ-ГГГГ'")
    except ValueError as ve:
        print(ve)


class Date:
    def __init__(self, date):
        self.date = date_format(date)

    @classmethod
    def extract(cls, date):
        try:
            date_list = date_format(date).split("-")
            return int(date_list[0]), int(date_list[1]), int(date_list[2])
        except AttributeError:
            pass

    @staticmethod
    def validate(date):
        # Список "for validation"
        fv = Date.extract(date)
        try:
            d(fv[2], fv[1], fv[0])
            print(f'Дата "{date}" корректна')
        except ValueError:
            print(f'Дата "{date}" некорректна')
        except TypeError:
            pass


# Проверки
def check(value):
    print(f'Заводим следующие данные: "{value}"')
    print(Date(value).date)
    print(Date.extract(value))
    Date.validate(value)
    print()


# Корректные данные
check("20-12-2020")

# Данные с ошибкой в формате
check("20-12-20200")

# Данные с ошибкой в дате
check("20-13-2020")
