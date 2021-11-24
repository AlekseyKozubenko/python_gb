"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_number_str = input("Введите целое положительное число: ")
user_number = int(user_number_str)
count = len(user_number_str)
max_number = 0
while count > 0:
    count -= 1
    temp_num = user_number // 10**count
    if max_number < temp_num:
        max_number = temp_num
    user_number = user_number - temp_num * 10**count

print(max_number)


