"""
Создайте класс `Car`, наследник `Vehicle`
"""
from engine import Engine
from base import Vehicle

class Car(Vehicle):
     
    engine: Engine

    def setEngine(self,engine:Engine):
        Car.engine = engine

"""audi = Car()
engine = Engine(1, 0.8)
audi.setEngine(engine)
audi.start()
"""