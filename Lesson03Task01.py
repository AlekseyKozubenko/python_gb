"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def my_func_divide(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Введите числа.")
        return None
    if b == 0:
        print("Знаменатель должен отличаться от нуля.")
        return None
    else:
        return a / b


arg_1 = input("Введите числитель: ")
arg_2 = input("Введите знаменатель: ")

print(my_func_divide(arg_1, arg_2))
