class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        perimeter = (self.length + self.width) * 2
        print(perimeter)

    def Area(self):
        area = self.length * self.width
        print(area)

    def display(self):
        print("""
        length: {}
        width: {}
        perimeter: {}
        area: {}
        """.format(self.length, self.width, self.Perimeter(), self.Area()))

dikdortgen = Rectangle(10, 4)
dikdortgen.Perimeter()
dikdortgen.Area()
dikdortgen.display()

class Parallelpipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        volume = self.length * self.width * self.height
        print(volume)


dikdortgen2 = Parallelpipede(10, 5, 6)
dikdortgen2.volume()
        