class Geometry():
    def __init__(self):
        pass

    def distance(self, a1, b1, a2, b2):
        distance = ((a1 - a2) ** 2 + (b1 - b2) ** 2) ** 0.5
        print(distance)

    def middle(self, a1, b1, a2, b2):
        a3 = (a1 + a2) // 2
        b3 = (b1 + b2) // 2
        print("orta: ({}, {})".format(a3, b3))

    def trianglePerimeter(self, a, b, c):
        perimeter = a + b + c
        print(perimeter)

    def triangelisoscel(self, a, b, c):
        if((a == b) or (a == c) or (b == c)):
            print("Üçgen ikizkenardır")

        else:
            print("üçgen ikizkenar değildir")


g = Geometry()
g.distance(5, 4, 1, 2)
g.middle(5, 4, 1, 2)
g.trianglePerimeter(1,2,3)
g.triangelisoscel(1,2,1)
