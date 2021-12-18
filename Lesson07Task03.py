"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
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
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, cells_count):
        self.cells_count = cells_count

    def __add__(self, other):
        return Cell(self.cells_count + other.cells_count)

    def __sub__(self, other):
        if self.cells_count <= other.cells_count:
            print("Вычитание невозможно.")
        else:
            return Cell(self.cells_count - other.cells_count)

    def __mul__(self, other):
        return Cell(self.cells_count * other.cells_count)

    def __truediv__(self, other):
        if self.cells_count < other.cells_count:
            print("Целочисленное деление невозможно.")
        else:
            return Cell(round(self.cells_count / other.cells_count))

    def make_order(self, cells_in_row):
        x = ""
        if self.cells_count % cells_in_row == 0:
            counter = int(self.cells_count / cells_in_row) - 1
            for i in range(counter):
                x = x + "*" * cells_in_row + "\n"
            remainder = self.cells_count - cells_in_row * counter
            x = x + "*" * remainder
            return x
        else:
            counter = int(self.cells_count / cells_in_row)
            for i in range(counter):
                x = x + "*" * cells_in_row + "\n"
            remainder = self.cells_count - cells_in_row * counter
            x = x + "*" * remainder
            return x


c1 = Cell(12)
c2 = Cell(15)
print("Клетка 1")
print(c1.make_order(7))
print("---")
print("Клетка 2")
print(c2.make_order(7))
print("---")
print("Сложение")
print((c1 + c2).make_order(7))
print("---")
print("Вычитание К1 - К2")
try:
    print((c1 - c2).make_order(7))
except AttributeError:
    print("Операция не выполнена")
print("---")
print("Вычитание К2 - К1")
try:
    print((c2 - c1).make_order(7))
except AttributeError:
    print("Операция не выполнена")
print("---")
print("Умножение")
print((c2 * c1).make_order(7))
print("---")
print("Деление К1 / К2")
try:
    print((c1 / c2).make_order(7))
except AttributeError:
    print("Операция не выполнена")
print("---")
print("Деление К2 / К1")
try:
    print((c2 / c1).make_order(7))
except AttributeError:
    print("Операция не выполнена")
print("---")

