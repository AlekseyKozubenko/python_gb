"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда).
Опишите несколько дочерних классов:
TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = None

    def go(self):
        print(f"Машина {self.name} поехала.")

    def stop(self):
        print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        self.direction = direction

    def show_speed(self):
        print(f"Скорость {self.name} - {self.speed}.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} превысила допустимую скорость 60 и двигается со скоростью {self.speed}.")
        else:
            print(f"Скорость {self.name} - {self.speed}.")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} превысила допустимую скорость 40 и двигается со скоростью {self.speed}.")
        else:
            print(f"Скорость {self.name} - {self.speed}.")


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = is_police


police = PoliceCar(100, "white", "police")
sport = SportCar(200, "red", "sport")
town_1 = TownCar(50, "grey", "town")
town_2 = TownCar(70, "yellow", "crazy_town")
work = WorkCar(30, "brown", "worker")
print(f"{police.name}, {police.color}, {police.speed}, {police.is_police}")
print(f"{work.name}, {work.color}, {work.speed}, {work.is_police}")

town_2.go()
town_2.turn("налево")
town_2.show_speed()
police.go()
police.turn("налево")
police.show_speed()
town_2.stop()
police.stop()
sport.show_speed()
