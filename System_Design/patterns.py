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
"""
The Singleton is a creational design pattern which ensures that at most one 
instance of a class may exist.

Singleton getInstance() will return the singleton instance.
String getValue() will return the value of the singleton.
void setValue(String value) will update the value of the singleton.
You can assume the singleton will only be used in a single-threaded environment.
"""	
class Singleton:
    _unique_instance = None

    def __new__(cls):
        if cls._unique_instance is None:
            cls._unique_instance = super(Singleton, cls).__new__(cls)

        return cls._unique_instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value

# Builder Pattern       	
"""
The Builder is a creational design pattern
 that allows the construction of complex objects step by step.
 It is useful when an object has several components and it's desirable 
 to construct the object with various configurations.

"""
class Meal:
    def __init__(self):
        self.cost = 0.0
        self.takeOut = False
        self.main = ""
        self.drink = ""

    def getCost(self) -> float:
        return self.cost

    def setCost(self, cost) -> None:
        self.cost = cost

    def getTakeOut(self) -> bool:
        return self.takeOut

    def setTakeOut(self, takeOut) -> None:
        self.takeOut = takeOut

    def getMain(self) -> str:
        return self.main

    def setMain(self, main) -> None:
        self.main = main

    def getDrink(self) -> str:
        return self.drink

    def setDrink(self, drink) -> None:
        self.drink = drink


class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def addCost(self, cost) -> 'MealBuilder':
        self.meal.setCost(cost)
        return self

    def addTakeOut(self, takeOut) -> 'MealBuilder':
        self.meal.setTakeOut(takeOut)
        return self

    def addMainCourse(self, main) -> 'MealBuilder':
        self.meal.setMain(main)
        return self

    def addDrink(self, drink) -> 'MealBuilder':
        self.meal.setDrink(drink)
        return self

    def build(self) -> Meal:
        return self.meal
    
# Prototype Pattern   	
"""
The Prototype is a creational design pattern that allows 
an object to copy itself. It is particularly useful when 
the creation of an object is more convenient through copying 
an existing object than through creation from scratch.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Shape:
        return Square(self.length)

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Shape:
        return Rectangle(self.width, self.height)

class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        return [shape.clone() for shape in shapes]

# Adapter Pattern   	
"""
The Adapter is a structural design pattern that allows incompatible
 interfaces to work together. It wraps an existing class with a new 
 interface so that it becomes compatible with the client's interface.
"""

class Square:
    def __init__(self, sideLength=0.0):
        self.sideLength = sideLength

    def getSideLength(self) -> float:
        return self.sideLength
    
class SquareHole:
    def __init__(self, sideLength: float):
        self.sideLength = sideLength

    def canFit(self, square: Square):
        return self.sideLength >= square.getSideLength()

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def getRadius(self):
        return self.radius

class CircleToSquareAdapter(Square):
    def __init__(self, circle: Circle):
        self.circle = circle

    def getSideLength(self) -> float:
        return 2 * self.circle.getRadius()

# Decorator Pattern   
"""
The Decorator is a structural design pattern that allows
 behavior to be added to individual objects, either statically 
 or dynamically, without affecting the behavior of other objects
from the same class.
""" 
class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self) -> float:
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self) -> float:
        return self.decoratedCoffee.getCost()

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def getCost(self) -> float:
        return super().getCost() + 0.5

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def getCost(self) -> float:
        return super().getCost() + 0.2

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def getCost(self) -> float:
        return super().getCost() + 0.7     	
    
# Facade Pattern       	
"""
The Facade is a structural design pattern that provides
a simplified interface to a complex system of classes,
library, or framework. It wraps the complexities of
the system and provides a simple interface to clients.
"""
class Order:
    def __init__(self, contents: str, takeOut: bool):
        self.contents = contents
        self.takeOut = takeOut

    def getOrder(self) -> str:
        return self.contents

    def isTakeOut(self) -> bool:
        return self.takeOut

class Cashier:
    def takeOrder(self, contents: str, takeOut: bool) -> Order:
        return Order(contents, takeOut)

class Food:
    def __init__(self, order: str):
        self.contents = order

    def getFood(self) -> str:
        return self.contents

class Chef:
    def prepareFood(self, order: Order) -> Food:
        return Food(order.getOrder())

class PackagedFood(Food):
    def __init__(self, food: Food):
        super().__init__(food.getFood() + " in a bag")

class KitchenStaff:
    def packageOrder(self, food: Food) -> PackagedFood:
        return PackagedFood(food)

class DriveThruFacade:
    def __init__(self):
        self.cashier = Cashier()
        self.chef = Chef()
        self.kitchenStaff = KitchenStaff()

    def takeOrder(self, orderContents: str, takeOut: bool) -> Food:
        order = self.cashier.takeOrder(orderContents, takeOut)
        food = self.chef.prepareFood(order)
        if order.isTakeOut():
            return self.kitchenStaff.packageOrder(food)
        return food

# Strategy Pattern   

"""
The Strategy is a behavioral design pattern that enables selecting an 
algorithm's runtime behavior. It defines a family of algorithms, 
encapsulates each one, and makes them interchangeable.
""" 
class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married

class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool:
        ...

class AdultFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.getAge() >= 18

class SeniorFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.getAge() >= 65

class MarriedFilter(PersonFilter):
    def apply(self, person: Person) -> bool:
        return person.isMarried()

class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        count = 0
        for person in people:
            if self.filter.apply(person):
                count += 1
        return count    	

# Observer Pattern      

"""
The Observer is a behavioral design pattern that allows 
objects to be notified about changes in another object's state.
""" 	
class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.observers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def updateStock(self, newStock: int) -> None:
        oldStock = self.stock
        self.stock = newStock

        if oldStock == 0 and newStock > 0:
            self.notifyObservers()

    def notifyObservers(self) -> None:
        for observer in self.observers:
            observer.notify(self.itemName)
# State Pattern  
"""
The State is a behavioral design pattern that allows an 
object to alter its behavior when its internal state changes.
 This pattern is often used to encapsulate the state-related 
 behavior within state-specific classes, avoiding large conditional
statements in the object's methods.
"""
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle_request(self, doc) -> None:
        pass

class Document:
    def __init__(self):
        self.state = Draft()
        self.approved = False

    def get_state(self) -> State:
        return self.state

    def set_state(self, state: State) -> None:
        self.state = state

    def publish(self) -> None:
        self.state.handle_request(self)

    def set_approval(self, approved: bool) -> None:
        self.approved = approved

    def is_approved(self) -> bool:
        return self.approved

class Draft(State):
    def handle_request(self, doc: Document) -> None:
        doc.set_state(Review())

class Review(State):
    def handle_request(self, doc: Document) -> None:
        if doc.is_approved():
            doc.set_state(Published())
        else:
            doc.set_state(Draft())

class Published(State):
    def handle_request(self, doc: Document) -> None:
        # Final state, no action needed
        pass     