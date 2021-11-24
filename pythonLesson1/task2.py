"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
from time import time

user_seconds = int(input("Введите время в секундах, для перевода в формат 'чч:мм:сс': "))

hours = user_seconds // (60 * 60)
minutes = user_seconds % (60 * 60) // 60
seconds = user_seconds - hours * 60 * 60 - minutes * 60
result = time()
print(f"{hours:02}:{minutes:02}:{seconds:02}")
#testing = hours * 3600 + minutes * 60 + seconds - Проверка 
#print(testing)
