# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод init()), который должен принимать данные (список списков)
# для формирования матрицы.     [[], [], []]
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
# в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
#
# Пример:
# 1 2 3
# 4 5 6
# 7 8 9
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# Сумма матриц:
# 2 4 6
# 8 10 12
# 14 16 18
import copy
from typing import List


class Matrix:
    def __init__(self, list_of_lists: List[List]):
        if type(list_of_lists) is not list:
            raise ValueError("class want only typesed arg - List!")
        if type(list_of_lists[0]) is not list:
            raise ValueError("class want only typesed arg - List!")

        self.matrix_data = list_of_lists

    def __str__(self):
        good_formatted = '\n'.join(' '.join(map(str, sl)) for sl in
                                   self.matrix_data)
        return good_formatted

    def __check_matrix_sizes(self, other_matrix):
        if len(self.matrix_data) != len(other_matrix.matrix_data) \
                or len(self.matrix_data[0]) != \
                len(other_matrix.matrix_data[0]):
            return False
        return True

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("add func only for matrix classes")
        if not self.__check_matrix_sizes(other):
            raise ValueError("for addition matrixes need keep "
                             "sizes columns and rows")

        list_of_lists = copy.deepcopy(other.matrix_data)

        for rrow in range(0, len(list_of_lists)):
            for columnn in range(0, len(list_of_lists[rrow])):
                list_of_lists[rrow][columnn] = self.matrix_data[rrow][
                                                   columnn] + \
                                               other.matrix_data[rrow][columnn]

        return Matrix(list_of_lists)


if __name__ == '__main__':
    # matrix = Matrix(6)
    matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    print(f"Inputed matrix \n{matrix}")

    second_matrix = Matrix([[7, 8], [9, 10], [11, 12]])
    print(f"Second matrix \n{second_matrix}")

    new_result_matrix = matrix + second_matrix
    print(f"Sum two matrixes \n{new_result_matrix}")
