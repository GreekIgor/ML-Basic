"""
Создайте dataclass `Engine`
"""
from dataclasses import dataclass

@dataclass
class Engine:
    volume: float
    pistons: int

    def __init__(self, volume, pistons):
        self.pistons = pistons
        self.volume = volume
