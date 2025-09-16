# Factory Method Pattern 
"""
The Factory Method is a creational design pattern that provides an interface 
for creating objects in a superclass but allows subclasses to alter the type 
of objects that will be created.
"""
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Bike()

class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()
  	
# Singleton Pattern       	
# Builder Pattern       	
# Prototype Pattern   	
# Adapter Pattern   	
# Decorator Pattern       	
# Facade Pattern       	
# Strategy Pattern       	
# Observer Pattern       	
# State Pattern       