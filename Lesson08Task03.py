"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class CheckDigit(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
while True:
    element = input("Введите число ('q' для выхода): ")
    if element == 'q':
        print("Конец программы.")
        break
    else:
        try:
            if element.isdigit():
                my_list.append(float(element))
            else:
                raise CheckDigit("Необходимо ввести число.")
        except CheckDigit as e:
            print(e)
        continue
print(my_list)
