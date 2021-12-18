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


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        s = ""
        for row in self.data:
            s += str(row) + "\n"
        return s

    # def __add__(self, other):
    #     result = []
    #     x = 0
    #     while x < len(self.data):
    #         row = []
    #         for i, j in zip(self.data[x], other.data[x]):
    #             row.append(i + j)
    #         result.append(row)
    #         x += 1
    #     return Matrix(result)

    def __add__(self, other):
        result = []
        for x, y in zip(self.data, other.data):
            row = []
            for i, j in zip(x, y):
                row.append(i + j)
            result.append(row)
        return Matrix(result)

m1 = Matrix([[1, 2, 3], [4, 5, 6], [8, 8, 8]])
print(m1)
m2 = Matrix([[6, 5, 4], [3, 2, 1], [2, 2, 2]])
print(m2)
m3 = m1 + m2
print(m3)
