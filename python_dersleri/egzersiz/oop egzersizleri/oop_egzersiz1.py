"""Write a Python program to create a Vehicle class with max_speed and mileage instance attributes."""

class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

mustang = Vehicle(320, 13165461 )

print(mustang.max_speed)
print(mustang.mileage)
