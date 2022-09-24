from unicodedata import name

"""Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it."""

class Vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:",bus.name,"Speed:",bus.max_speed,"Mileage:",bus.mileage)        