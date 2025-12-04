"""
Создайте класс `Plane`, наследник `Vehicle`
"""
import exceptions
from base import Vehicle

class Plane(Vehicle):

  def __init__(self,weight, started, fuel, fuel_consumption, max_cargo = 100):
    super().__init__(weight, started, fuel, fuel_consumption)
    self.max_cargo  = max_cargo
    self.cargo = 0

  def load_cargo(self, load:int):
    if(load + self.cargo)>self.max_cargo:
      raise exceptions.CargoOverload(message = 'Транспорт перегружен')
    self.cargo = load

  def remove_all_cargo(self):
    prev_cargo = self.cargo
    self.cargo = 0
    return prev_cargo 
  

"""plane = Plane(700,False, 300, 140,100)
plane.load_cargo(100)
print(plane.remove_all_cargo())
plane.load_cargo(500)
"""