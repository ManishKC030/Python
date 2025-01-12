#Abstraction focuses on hiding complex implementation details and showing only the essential features of an object.
# Python achieves abstraction using abstract base classes (ABCs).

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car is starting."

class Bike(Vehicle):
    def start(self):
        return "Bike is starting."

vehicles = [Car(), Bike()]
for vehicle in vehicles:
    print(vehicle.start())  # Outputs: Car is starting.
                                      #Bike is starting


