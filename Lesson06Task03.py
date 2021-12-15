"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

# Попробовал сделать __income, но он не унаследовался в дочернем классе


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"Полное имя сотрудника: {self.name} {self.surname}."

    def get_total_income(self):
        return f"Сумма дохода: {sum(self._income.values())}."


boss = Position("Bob", "Smith", "Boss", 1000, 300)
print(boss.get_full_name())
print(boss.get_total_income())
print(boss.name)
print(boss.surname)
print(boss.position)
print(boss._income)
boss.name = "NotBob"
boss._income = {"wage": 0, "bonus": 0}
print(boss.get_full_name())
print(boss.get_total_income())
