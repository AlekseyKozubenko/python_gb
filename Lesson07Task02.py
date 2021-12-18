"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    # types = ["пальто", "костюм"]

    @abstractmethod
    def __init__(self, title, size, type_of):
        self.title = title
        self.type_of = type_of
        self.size = size

    @abstractmethod
    def expenditure(self):
        pass


class Coat(Clothes):
    def __init__(self, title, size, type_of="пальто"):
        self.title = title
        self.type_of = type_of
        self.size = size

    @property
    def expenditure(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, title, size, type_of="костюм"):
        self.title = title
        self.type_of = type_of
        self.size = size

    @property
    def expenditure(self):
        return self.size * 2 + 0.3


coat_1 = Coat("GUCCI", 42)
costume_1 = Costume("шерстяной", 1.61)

print(f"Затраты ткани на {coat_1.type_of} {coat_1.title} размером {coat_1.size} составит {coat_1.expenditure:.2f}")
print(f"Затраты ткани на {costume_1.type_of} {costume_1.title} на рост {costume_1.size}м "
      f"составит {costume_1.expenditure:.2f}")
