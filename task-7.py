"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, real_number, imaginary_unit):
        self.real_number, self.imaginary_unit = real_number, imaginary_unit

    def __add__(self, other):
        return ComplexNumber(self.real_number + other.real_number, self.imaginary_unit + other.imaginary_unit)

    def __mul__(self, other):
        return ComplexNumber(self.real_number * other.real_number - self.imaginary_unit * other.imaginary_unit,
                             self.real_number * other.imaginary_unit - self.imaginary_unit * other.real_number)

    def __str__(self):
        return f'{self.real_number} + {self.imaginary_unit}j'


complex_number_1 = ComplexNumber(6, 3)
complex_number_2 = ComplexNumber(8, -9)

print(f'complex_number_1 = {complex_number_1}')
print(f'complex_number_2 = {complex_number_2}')
print(f'complex_number_1 + complex_number_2 = {complex_number_1 + complex_number_2}')
print(f'complex_number_1 * complex_number_2 = {complex_number_1 * complex_number_2}')