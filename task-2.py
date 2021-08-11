"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param: float):
        if param < 0:
            print("Принимаются только положительные числа")
            return
        else:
            self.param = param

    @abstractmethod
    def cloth_consumption(self):
        pass

    @abstractmethod
    def print_consumption(self):
        pass


class Coat(Clothes):
    @property
    def cloth_consumption(self):
        return self.param / 6.5 + 0.5

    @property
    def print_consumption(self):
        print(f'Расход ткани на пальто размером {self.param} равно {self.cloth_consumption}')


class Costume(Clothes):
    @property
    def cloth_consumption(self):
        return 2 * self.param + 0.3

    @property
    def print_consumption(self):
        print(f'Расход ткани на костюм для роста {self.param} равно {self.cloth_consumption}')


Coat(50).print_consumption
Costume(1.8).print_consumption
print(f'Общий расход ткани равен {Coat(50).cloth_consumption + Costume(1.8).cloth_consumption}')
