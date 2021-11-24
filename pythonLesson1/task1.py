"""
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и
сохраните в переменные, выведите на экран.
"""

num = 123
text = "some text"
condition = True
my_list = ["ball", "sneakers", "field"]
my_tuple = ("login", "password")
my_dict = {"1": "Jan", "2": "Feb", "3": "Mar"}
list2print = [num, text, condition, my_dict, my_list, my_tuple]

i = 0
y = len(list2print)
while i < y:
    a = list2print[i]
    print(f"Тип объекта: {type(a)}, содержание:  {a}")
    i += 1

user_name = input("Введите Ваше имя: ")
user_year = int(input("Введите год Вашего рождения: "))
print(f"Привет, {user_name}! Могу угадать твой возраст - примерно {2021 - user_year} лет")