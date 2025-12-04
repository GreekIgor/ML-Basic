"""
Доработайте класс `Vehicle`
"""

from abc import ABC
from exceptions import *


class Vehicle(ABC):
    
    def __init__(self, weight = 1000, started = False, fuel = 10, fuel_consumption = 10):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == False and self.fuel>0:
            print(f'Все хорошо запускаем двигатель')
        else:
            raise LowFuelError(message= 'Запуск не возможен нету топлива')
        
    def move(self, distance):
        if self.fuel< (distance * self.fuel_consumption):
            raise NotEnoughFuel(message= 'Не достаточно топлива для преодоления дистанции')
        self.fuel -= (distance * self.fuel_consumption)
        print(f"Растояние ${distance} осталость топливо ${self.fuel}")
        pass


