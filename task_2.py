# Реализовать программу работы с органическими клетками, состоящими из ячеек.
#
# Необходимо создать класс Клетка (Cell).
# В его конструкторе инициализировать параметр (quantity),
# соответствующий количеству ячеек клетки (целое число).
#
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()),             вычитание (sub()),          умножение (mul()),
# деление (truediv()).
#
# Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого)
# деление клеток, соответственно.
#
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#
# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#
# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# ** - По желанию: В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида \n\n*...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: \n\n.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: **\n\n*.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.
#
# Пример клиентского кода:
# print("Создаем объекты клеток")
# cell1 = Cell(30)
# cell2 = Cell(25)
#
# cell3 = Cell(10)
# cell4 = Cell(15)
#
# print()
#
# print("Складываем")
# print(cell1 + cell2)
#
# print()
#
# print("Вычитаем")
# print(cell2 - cell1)
# print(cell4 - cell3)
#
# print()
#
# print("Умножаем")
# print(cell2 * cell1)
#
# print()
#
# print("Делим")
# print(cell1 / cell2)
#
# print()
#
# print("Организация ячеек по рядам")
# print(cell1.make_order(5))
# print(cell2.make_order(10))
#
# Результаты:
# Создаем объекты клеток
#
# Складываем
# Сумма клеток = (55)
#
# Вычитаем
# Разность отрицательна, поэтому операция не выполняется
# Разность клеток = (5)
#
# Умножаем
# Умножение клеток = (750)
#
# Делим
# Деление клеток = (1)
#
# Организация ячеек по рядам
# \n \n *\n *\n *\n *\n
# *\n **\n **
# """
# """
import sys


# For short line throws Exception
def throw_ex(ex):
    raise ex


class Cell:
    def __init__(self, quantity_cells: int):
        throw_ex(ValueError("int only")) \
            if type(quantity_cells) is not int else ()

        self.quantity = quantity_cells

    def __add__(self, other):
        self.is_destroyed()
        return self.quantity + other.quantity

    def __sub__(self, other):
        self.is_destroyed()

        new_quant = self.quantity - other.quantity
        throw_ex(ValueError(f"result {new_quant}. Impossible operation")) \
            if new_quant < 0 is not int else ()
        return Cell(new_quant)

    def __mul__(self, other):
        self.is_destroyed()

        new_cell = Cell(self.quantity * other.quantity)

        self.__del__()
        other.__del__()
        # print(sys.getrefcount(other))

        return new_cell

    def __truediv__(self, other):
        self.is_destroyed()

        new_cell = Cell(self.quantity // other.quantity)
        self.__del__()
        other.__del__()

        return new_cell

    def __str__(self):
        return f"Cell of {self.quantity} quantity"

    def __del__(self):
        self.quantity = None

    # Check cell (object) alreay destroyred
    def is_destroyed(self):
        throw_ex(NameError(f"object {self.__repr__()} destroyed already")) \
            if self.quantity == None else ()

    # def make_order(Cell,quant_in_row):
    #     sdf=0


#     At this point more effective class container for Cell class
#      or listener-decorator for all methods class

if __name__ == '__main__':
    cell_1 = Cell(30)
    cell_2 = Cell(25)

    cell_3 = Cell(10)
    cell_4 = Cell(15)

    print(cell_1)
    print(cell_2)
    print(cell_3)
    print(cell_4)

    print()

    print(f"Plus {cell_1}+{cell_2}")
    new_cell = cell_1 + cell_2
    print(f"new Cell created - quantity {new_cell}")

    print()
    print(f"Minus {cell_2}-{cell_1}")
    try:
        new_cell = cell_2 - cell_1
    except ValueError as val_err:
        print(val_err)

    print()
    print(f"Minus {cell_4}-{cell_3}")
    new_cell = cell_4 - cell_3
    print(f"new Cell created - quantity {new_cell}")

    print()
    print(f"Multiply {cell_2} and {cell_1}")
    new_cell = cell_1 * cell_2
    print(f"new Cell created - quantity {new_cell}")
    print(f"Two cells destroyed while process. "
          f"Quantiny of Cell first {cell_1.quantity}. "
          f"Quantity of Cell sec {cell_2.quantity}")

    cell_1 = Cell(30)
    cell_2 = Cell(25)

    print()
    print(f"Division {cell_1} on {cell_2}")
    new_cell = cell_1 / cell_2
    print(f"new Cell created - quantity {new_cell}")
    print(f"Two cells destroyed while process. "
          f"Quantiny of Cell first {cell_1.quantity}. "
          f"Quantity of Cell sec {cell_2.quantity}")
