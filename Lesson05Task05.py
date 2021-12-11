"""
 Создать (программно) текстовый файл, записать в него
 программно набор чисел,  разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from functools import reduce


with open("sum.txt", "w") as file_obj:
    file_obj.write(input("Введите числа через пробел: "))

sum_obj = open("sum.txt")
sum = sum_obj.read().split()

print(f"Сумма чисел в файле: {reduce((lambda x, y: int(x) + int(y)),sum)}")
