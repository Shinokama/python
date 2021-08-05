"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0

    def __init__(self, color, name, is_police: bool):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed: int):
        if self.speed == 0:
            print(f'Машина "{self.color} {self.name}" поехала')
        self.speed = speed

    def stop(self):
        self.speed = 0
        print(f'Машина "{self.color} {self.name}" остановилась')

    def turn(self, direction):
        print(f'Машина "{self.color} {self.name}" повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля "{self.color} {self.name}" равна {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости! Текущая скорость автомобиля "{self.color} {self.name}" '
                  f'равна {self.speed} км/ч')

        else:
            print(f'Текущая скорость автомобиля "{self.color} {self.name}" равна {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости! Текущая скорость автомобиля "{self.color} {self.name}" '
                  f'равна {self.speed} км/ч')

        else:
            print(f'Текущая скорость автомобиля "{self.color} {self.name}" равна {self.speed} км/ч')


class PoliceCar(Car):
    pass


cars = (TownCar("Красный", "Лада Калина", False),
        SportCar("Синий", "Subaru Impreza", False),
        WorkCar("Белый", "ГАЗЕЛЬ NEXT", False),
        PoliceCar("ДПС", "Skoda Octavia", True))

for car in cars:
    if car.is_police:
        print(f'\nПолицейский автомобиль, стиль окрашивания: {car.color}, модель: {car.name}')
    else:
        print(f'\nЦвет автомобиля: {car.color}, модель: {car.name}')
    car.go(30)
    car.show_speed()
    car.turn("направо")
    car.turn("налево")
    car.go(50)
    car.show_speed()
    car.go(70)
    car.show_speed()
    car.stop()
    car.show_speed()
