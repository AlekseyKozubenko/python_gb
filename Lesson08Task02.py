"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    divider = input("Необходимо разделить число '100', введите делитель ('q' для выхода): ")
    if divider == 'q':
        print("Конец программы.")
        break
    else:
        try:
            divider = int(divider)
        except ValueError:
            print("Введите число.")
            continue
        try:
            if divider == 0:
                raise ZeroDivision("Деление на нуль не допустимо.")
            else:
                print(f"Результат деления: {round(100 / divider, 2)}")
        except ZeroDivision as e:
            print(e)
