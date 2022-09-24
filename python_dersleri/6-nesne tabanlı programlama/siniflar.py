"""class Araba2():
    model = "Renault Megane"
    renk = "Gümüş"
    beygirGucu = 110
    silindir = 4

    def __init__(self):
        print("init fonksiyonu çağrıldı")


araba99 = Araba2()
araba98 = Araba2()
araba99.renk = "Siyah"
print(araba99.renk)
print(Araba2.model)
print(dir(araba99))"""


class Araba():
    def __init__(self, model = "Bilgi Yok", renk = "Bilgi Yok", beygirGucu = "Bilgi Yok", silindir = "Bilgi Yok"):
        print("init fonksiyonu çağrıldı")
        self.model = model
        self.renk = renk
        self.beygirGucu = beygirGucu
        self.silindir = silindir


araba1 = Araba("Renault Megane", "Gümüş", 110, 4)
araba2 = Araba("Peugeot", "Beyaz", 90, 4)
araba3 = Araba(beygirGucu=150)

print(araba1.model)
print(araba2.model)
print(araba3.model)
print(araba3.beygirGucu)
