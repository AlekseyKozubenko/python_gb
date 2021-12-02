"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


# Возведение в степень с помощью **
def my_func(x, y):
    return x**y


# Для вычисления числа в отрицательной степени необходимо "1" разделить на число в степени по модулю
def my_func_v2(x, y):
    denominator = x
    i = 1
    while i < abs(y):
        denominator *= x
        i += 1
    return 1 / denominator


while True:
    try:
        x = float(input("Введите действительное положительное число для основания степени: "))
        if x <= 0:
            print("Требуется положительное действительное число!")
            continue
        y = int(input("Ведите целое отрицательное число для числа степени: "))
        if y > 0:
            print("Требуется отрицательное значение для числа степени!")
            continue
        break
    except ValueError:
        print("Введите число!")
        continue

print(my_func(x, y))
print(my_func_v2(x, y))
