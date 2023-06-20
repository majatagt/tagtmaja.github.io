# exercise one: create a Class with instance attributes
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


model1 = Vehicle("Car1", 200, 421)
print(model1.name, model1.max_speed, model1.mileage)


# create childclass bus that inherits from Vechicle class
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


# create childclass that will inherit from Vehicle class
Shuttle_bus = Bus("Airport bus", 55, 360)
print(Shuttle_bus.name, Shuttle_bus.max_speed, Shuttle_bus.mileage)

# create a Bus class that inherits from the Vehicle class.
# ive the capacity argument of Bus.seating_capacity() a default value of 50
print(Shuttle_bus.seating_capacity())


# Define a class attribute”color” with a default value white.
# i.e., Every Vehicle should be white.
class Vehicle1:
    colour = "Blue"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle1):
    pass


class Car(Vehicle1):
    pass


Shuttle_bus1 = Bus("Airport shuttle", 40, 2550)
print(Shuttle_bus1.colour,Shuttle_bus1.name, "Speed:", Shuttle_bus1.max_speed, "Mileage:", Shuttle_bus1.mileage)

car = Car("Peugot", 56, 10254)
print(car.colour, car.name,"Speed:", car.max_speed, "Mileage:", car.mileage)


# The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance,
# we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance
# will become the final amount = total fare + 20% of the total fare.
#
# Note: The bus seating capacity is 50. so the final fare amount should be 6000.
# You need to override the fare() method of a Vehicle class in Bus class.
#
# Use the following code for your parent Vehicle class.
# We need to access the parent class from inside a method of a child class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
        def fare(self):
            amount = super().fare()
            amount += amount * 20 / 100
            return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())


class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


# Check type of an object
# Write a program to determine which class a given Bus object belongs to.
class Bus(Vehicle):
    pass

School_bus2 = Bus("School Volvo", 12, 50)
print(type(School_bus2))