"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        view = '\n'
        for string in self.matrix:
            for el in string:
                view += f'\t{el}\t'
            view += '\n'
        return view

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            print("Матрицы имеют разное количество строк, сложение невозможно")
        else:
            new = []
            for row_num in range(len(self.matrix)):
                if len(self.matrix[row_num]) != len(other.matrix[row_num]):
                    print("Матрицы имеют разное количество столбцов, сложение невозможно")
                    return
                else:
                    string = []
                    for column_num in range(len(self.matrix[row_num])):
                        string.append(self.matrix[row_num][column_num] + other.matrix[row_num][column_num])
                    new.append(string)
            return Matrix(new)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9, 0]])
matrix_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_4 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(f'matrix_1: {matrix_1}\nmatrix_2: {matrix_2}\nmatrix_3: {matrix_3}\nmatrix_4: {matrix_4}\n')
print(f'matrix_1 + matrix_2: {matrix_1 + matrix_2}')
print(f'matrix_1 + matrix_3: {matrix_1 + matrix_3}')
print(f'matrix_1 + matrix_4: {matrix_1 + matrix_4}')
