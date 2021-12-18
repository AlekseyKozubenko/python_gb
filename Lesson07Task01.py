"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""


class MatrixError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Matrix:
    def __init__(self, data):
        self.data = data
        print("Создан объект матрица")

    @staticmethod
    def is_matrix(data):
        # self.data = data
        try:
            if type(data) == list:
                columns_num = len(data[0])
                for el in data:
                    if type(el) == list and len(el) == columns_num:
                        for num in el:
                            if type(num) == int:
                                pass
                            else:
                                raise MatrixError("Введите числа.")
                    else:
                        raise MatrixError("Не корректная длина ряда")
                return Matrix(data)
            else:
                raise MatrixError("Данные не корректные")
        except MatrixError as err:
            print(err)
            return

    def __del__(self):
        print("Матрица удалена")

    def matrix_size(self):
        return f"{len(self.data)} x {len(self.data[0])}"

    def __str__(self):
        s = ""
        for row in self.data:
            s += str(row) + "\n"
        return s

    def __add__(self, other):
        if self.matrix_size() != other.matrix_size():
            print("Размеры матриц не совпадают.")
        else:
            result = []
            x = 0
            while x < len(self.data):
                row = []
                for i, j in zip(self.data[x], other.data[x]):
                    row.append(i + j)
                result.append(row)
                x += 1
            return Matrix(result)


m1 = [[1, 2, 3], [4, 5, 6]]
m1 = Matrix.is_matrix(m1)
print(m1)
m2 = [[1, 2, 3], [4, 5]]
m2 = Matrix.is_matrix(m2)
print(m2)
# print(m2.matrix_size())
m3 = 6
m3 = Matrix.is_matrix(m3)
print(m3)
m4 = [[1, 2, 3], ["f", 5, 8]]
m4 = Matrix.is_matrix(m4)
print(m4)
m5 = [[1, 2, 3], [4, 5, 6], [8, 8, 8]]
m5 = Matrix.is_matrix(m5)
print(m5)
m6 = [[6, 5, 4], [3, 2, 1], [2, 2, 2]]
m6 = Matrix.is_matrix(m6)
print(m6)
m7 = m5 + m6
print(m7)
m8 = m5 + m1
