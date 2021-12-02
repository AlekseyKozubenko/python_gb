"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


# Сравниваю каждый элемент с парой других
def my_func(a, b, c):
    if a <= b and a <= c:
        return b + c
    elif b <= c and b <= a:
        return c + a
    else:
        return a + b


# Суммирую три числа и вычитаю наименьший
def my_func_v2(a, b, c):
    my_list = [a, b, c]
    return sum(my_list) - min(my_list)


print(my_func(1, 10, 1000))
print(my_func_v2(1, 10, 1000))
