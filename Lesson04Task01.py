"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт
с параметрами.
"""

from sys import argv

script_name, hours, rate, premium = argv


def salary(a, b, c):
    try:
        a, b, c = float(a), float(b), float(c)
    except ValueError:
        print("Введите числовые значения.")
        return
    return a * b + c


print(f"Сумма заработной платы составила: {salary(hours, rate, premium)}")
