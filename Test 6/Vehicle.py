
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, no_of_persons):
        self.no_of_persons = no_of_persons

    @abstractmethod
    def calculate_toll(self):
        pass

class TwoWheeler(Vehicle):
    def calculate_toll(self):
        basictoll = 20
        extra_charge = 0
        if (self.no_of_persons > 2):
            extra_charge = (self.no_of_persons - 2) * 10
        return basictoll + extra_charge

class ThreeWheeler(Vehicle):
    def calculate_toll(self):
        basictoll = 30
        extra_charge = 0
        if (self.no_of_persons > 3):
            extra_charge = (self.no_of_persons - 3) * 20
        return basictoll + extra_charge

class FourWheeler(Vehicle):
    def calculate_toll(self):
        basictoll = 40
        extra_charge = 0
        if (self.no_of_persons > 4):
            extra_charge = (self.no_of_persons - 4) * 40
        return basictoll + extra_charge

class HeavyVehicle(Vehicle):
    def calculate_toll(self):
        basictoll = 60
        extra_charge = 0
        if (self.no_of_persons > 6):
            extra_charge = (self.no_of_persons - 6) * 60
        return basictoll + extra_charge