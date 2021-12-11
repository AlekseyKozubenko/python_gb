"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open("salary.txt", "r", encoding="utf-8") as file_obj:
    content = file_obj.readlines()
    salary_dict = {}
    result_list = []
    for row in content:
        name = row.split()[0]
        salary_value = int(row.split()[1])
        salary_dict[name] = salary_value
        if salary_value < 20000:
            result_list.append(name)
print(f"Сотрудники с окладом менее 20 тыс: {result_list}")
print(f"Средняя величина оклада: {sum(salary_dict.values())/len(salary_dict)}")
