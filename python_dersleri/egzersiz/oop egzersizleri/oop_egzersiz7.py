"""Determine if School_bus is also an instance of the Vehicle class"""

class Vehicle():
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 12, 50)
print(isinstance(bus, Vehicle))

p, q, r = 10, 20, 30
print(p,q,r)