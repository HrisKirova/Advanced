from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass
    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):

    def drive(self, distance):
        self.fuel_consumption += 0.9
        distance_allowed = self.fuel_quantity / self.fuel_consumption
        if distance_allowed >= distance:
            self.fuel_quantity -= distance * self.fuel_consumption


    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):


    def drive(self, distance):
        self.fuel_consumption += 1.6
        distance_allowed = self.fuel_quantity / self.fuel_consumption
        if distance_allowed >= distance:
            self.fuel_quantity -= distance * self.fuel_consumption

    def refuel(self, fuel):
        fuel *= 0.95
        self.fuel_quantity += fuel

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
