"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import sys
import time
from itertools import cycle

# С помощью итератора CYCLE обхожу список цветов светофора
# Установлено ограничение на вывод 3-х циклов
# Делаю обратный отсчет для выведенного цвета


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 3
        print("Светофор выполнит 3 цикла.")
        for color in cycle(self.__color):
            if i < 1:
                break
            if color == self.__color[0]:
                print(color)
                for remaining in range(7, -1, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d}".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
            elif color == self.__color[1]:
                print(f"\n{color}")
                for remaining in range(2, -1, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d}".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
                # time.sleep(1)
            else:
                print(f"\n{color}")
                for remaining in range(5, -1, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d}".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
                print("\n")
                i -= 1


my_traffic_light = TrafficLight()
my_traffic_light.running()
