"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def numeric(cls):
        date = input("Введите число в виде Д-М-ГГГГ: ").split("-")
        try:
            date_list = [int(el) for el in date]
        except ValueError():
            print("Введите числа")
        Date.valid_date(date_list[0], date_list[1], date_list[2])
        return Date("-".join([str(el) for el in date_list]))

    @staticmethod
    def valid_date(day, month, year):
        if 1930 < year < 2050:
            pass
            # print("Год в диапазоне 1930 - 2050 гг")
        else:
            raise DateError("Год не входит в диапазон 1930 - 2050гг")
        if 0 < month < 13:
            pass
            # print("Месяц в диапазоне от 1 до 12")
        else:
            raise DateError("Номер месяца не входит в диапазон 1 - 12")
        if 1 > day or day > 31:
            raise DateError("Номер дня не входит в диапазон 1 - 31")
        elif month == 2 and day > 28:
            raise DateError("В Феврале не может быть более 28 дней")
        elif month in [4, 6, 9, 11] and day > 30:
            raise DateError("В апреле, июне, сентябре и ноябре не может быть более 30 дней")


try:
    d2 = Date.numeric()
    print(d2.str_date)
except DateError as e:
    print(e)
