"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке:
https://pythonworld.ru/osnovy/peregruzka-operatorov.html
"""


class Cell:
    def __init__(self, number: int):
        if number <= 0:
            print('Принимаются только положительные числа больше нуля')
        else:
            self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            print('Вычитание невозможно, так как первая клетка меньше второй')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        if self.number > other.number:
            return Cell(self.number // other.number)
        else:
            print('Деление невозможно, так как первая клетка меньше второй')

    def make_order(self, length):
        return ((length * '*') + '\n') * (self.number // length) + (self.number % length) * '*'


cell_1 = Cell(4)
cell_2 = Cell(8)
cell_3 = Cell(-1)

print(f'\ncell_1:\n{cell_1.make_order(5)}\ncell_2:\n{cell_2.make_order(5)}')

print(f'\ncell_1 + cell_2:\n{(cell_1 + cell_2).make_order(5)}')

print('\ncell_1 - cell_2:')
cell_sub_1 = cell_1 - cell_2
try:
    print(cell_sub_1.make_order(5))
except AttributeError:
    pass

print('\ncell_2 - cell_1:')
cell_sub_2 = cell_2 - cell_1
try:
    print(cell_sub_2.make_order(5))
except AttributeError:
    pass

print(f'\ncell_1 * cell_2:\n{(cell_1 * cell_2).make_order(5)}')

print('\ncell_1 / cell_2:')
cell_truediv_1 = cell_1 / cell_2
try:
    print(cell_truediv_1.make_order(5))
except AttributeError:
    pass

print('\ncell_2 / cell_1:')
cell_truediv_2 = cell_2 / cell_1
try:
    print(cell_truediv_2.make_order(5))
except AttributeError:
    pass
