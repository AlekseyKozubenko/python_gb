"""
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и
общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re
# from time import process_time

# start1 = process_time()
result_dict = {}

# Для формирования словаря нужны Ключ и Значение
# Содержимое файла делю на строки, строки "сплитую" в список слов
# Для Ключа беру первый элемент из списка слов
# Чтобы сложить все числа, запускаю два цикла "for" - для слова в списке, для буквы в слове
# Нахожу цифры и добавляю их в переменную "num", которую потом преобразую в число и добавляю в список "value"
# Суммирую список "value" для Значения
with open("schedule.txt", "r", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
    # print(content)
    for string in content:
        word_list = string.split()
        # print(word_list)
        key = word_list[0].strip(":")
        value_list = []
        for word in word_list[1:]:
            num = ""
            for char in word:
                if char.isdigit():
                    num += char
            if num != "":
                value_list.append(int(num))
        # print(key)
        # print(sum(value_list))
        result_dict.update({key: sum(value_list)})

print(result_dict)
# stop1 = process_time()
# print(f"Время выполнения №1: {stop1 - start1}")

# Второй способ с помощью модуля "re"
# При замере времени выполнения это решение оказалось менее эффективным на 20% - 50%
# тестировал на файле с 90 тыс строк
# start2 = process_time()
result_dict_2 = {}
with open("schedule.txt", "r", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
    for string in content:
        key_2 = string.split()[0].strip(":")
        s = (re.sub("[^0-9]", " ", string)).split()
        value_2 = sum([int(el) for el in s])
        result_dict_2.update({key_2: value_2})
print(result_dict_2)
# stop2 = process_time()
# print(f"Время выполнения №2: {stop2 - start2}")
