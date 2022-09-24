import math


class Circle():
    def __init__(self, a, b, r):
        self.a = a  # merkezin a noktası
        self.b = b  # merkezin b noktası
        self.r = r  # yarıçap

    def Area(self):
        area = math.pi * (self.r ** 2)
        print("Alan:", area)

    def Perimeter(self):
        perimeter = 2 * math.pi * self.r
        print(perimeter)

    def testBelongs(self, x, y):
        uzaklik = ((x - self.a) ** 2 + (y - self.b) ** 2) ** 0.5
        if(uzaklik < self.r):
            print("Girdiğiniz noktalar çemberin içinde...")

        elif(uzaklik == self.r):
            print("Girdiğiniz noktalar çemberin tam üzerinde...")

        else:
            print("Girdiğiniz noktalar çemberin dışında...")


c = Circle(1,2,1)
c.Area()
c.Perimeter()
c.testBelongs(1,1)
