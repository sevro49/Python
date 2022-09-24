"""Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin."""


class Hayvan():
    def __init__(self, alem="Hayvanlar", sube="Omurgalılar"):
        print("Hayvan sınıfı init fonksiyonu")
        self.alem = alem
        self.sube = sube

    def bilgileriGoster(self):
        print("\n...Hayvanlar sınıfının bilgileri...")
        print("Âlem: {}\nŞube: {}\n".format(self.alem, self.sube))


hayvan = Hayvan()


class Kopek(Hayvan):
    def __init__(self, alem="Hayvanlar", sube="Omurgalılar", sinif="Memeliler", takim="Etçiller", familya="Köpekgiller", cins="Bilgi Yok", tur="Bilgi Yok"):
        super().__init__(alem, sube)
        print("Köpek sınıfı init fonksiyonu")
        self.sinif = sinif
        self.takim = takim
        self.familya = familya
        self.cins = cins
        self.tur = tur

    def havla(self):
        print("{}: Hav Hav !!".format(self.tur))

    def cinsBelirle(self, cins):
        self.cins = cins
        print(self.cins)

    def turBelirle(self, tur):
        self.tur = tur
        print(self.tur)

    def bilgileriGoster(self):
        print("\n\n...{} bilgileri...".format(self.tur))
        print("Âlem: {}\nŞube: {}\nSınıf: {}\nTakım: {}\nFamilya: {}\nCins: {}\nTür: {}\n".format(
            self.alem, self.sube, self.sinif, self.takim, self.familya, self.cins, self.tur))


husky = Kopek()
k9 = Kopek()
husky.cinsBelirle("Husky")
husky.turBelirle("Sibirya Kurdu")
husky.havla()
k9.havla()
k9.cinsBelirle("Alman Çoban Köpeği")
k9.turBelirle("ve GARİP KONT")
husky.bilgileriGoster()
k9.bilgileriGoster()

class Kus(Hayvan):
    def __init__(self, alem="Hayvanlar", sube="Omurgalılar", sinif="Kuşlar", takim="Sokak Kuşları", familya="Kuşgiller", cins="Bilgi Yok", tur="Bilgi Yok"):
        super().__init__(alem, sube)
        print("Kuş sınıfı init fonksiyonu")
        self.sinif = sinif
        self.takim = takim
        self.familya = familya
        self.cins = cins
        self.tur = tur

    def ot(self):
        print("{}: Cik Cik !!".format(self.tur))

    def cinsBelirle(self, cins):
        self.cins = cins
        print(self.cins)

    def turBelirle(self, tur):
        self.tur = tur
        print(self.tur)

    def bilgileriGoster(self):
        print("\n\n...{} bilgileri...".format(self.tur))
        print("Âlem: {}\nŞube: {}\nSınıf: {}\nTakım: {}\nFamilya: {}\nCins: {}\nTür: {}\n".format(
            self.alem, self.sube, self.sinif, self.takim, self.familya, self.cins, self.tur))

muhabbetKusu = Kus()
muhabbetKusu.cinsBelirle("Karga")
muhabbetKusu.turBelirle("Dadaş")
muhabbetKusu.bilgileriGoster()
muhabbetKusu.ot()

class At(Hayvan):
    def __init__(self, alem="Hayvanlar", sube="Omurgalılar", sinif="4 ayaklılar", takim="yarış atları", familya="atgiller", cins="Bilgi Yok", tur="Bilgi Yok"):
        super().__init__(alem, sube)
        print("At sınıfı init fonksiyonu")
        self.sinif = sinif
        self.takim = takim
        self.familya = familya
        self.cins = cins
        self.tur = tur

    def ot(self):
        print("{}: 'At sesi' !!".format(self.tur))

    def cinsBelirle(self, cins):
        self.cins = cins
        print(self.cins)

    def turBelirle(self, tur):
        self.tur = tur
        print(self.tur)

    def bilgileriGoster(self):
        print("\n\n...{} bilgileri...".format(self.tur))
        print("Âlem: {}\nŞube: {}\nSınıf: {}\nTakım: {}\nFamilya: {}\nCins: {}\nTür: {}\n".format(
            self.alem, self.sube, self.sinif, self.takim, self.familya, self.cins, self.tur))

duldul = At()
duldul.cinsBelirle("Redkit atı")
duldul.turBelirle("Beyaz redkit atı")
duldul.ot()
duldul.bilgileriGoster()