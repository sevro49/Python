class Calisan():
    def __init__(self, isim="Bilgi Yok!", maas="Bilgi Yok!", departman="Bilgi Yok!"):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):
        print("\n...Çalışan sınıfının bilgileri...")
        print("İsim: {}\nMaaş: {}\nDepartman: {}\n".format(
            self.isim, self.maas, self.departman))

    def departmanDegistir(self, yeniDepartman):
        self.departman = yeniDepartman


# Calisan sınıfının alt sınıfı olduğunu böyle gösterebiliriz.
class Yonetici(Calisan):
    pass  # fonksiyon içine bir şey yazmazsak python hata veriyor. sonradan bir şey yazacaksak pass kullanabiliriz. python sorun çıkartmıyor.

    def zamYap(self, zamMiktarı):
        print("Zam yapılıyor...")
        self.maas += zamMiktarı


#yonetici = Yonetici("Emre Güler", 10000, "Bilişim")
# yonetici.bilgileriGoster()
#yonetici.departmanDegistir("İnsan Kaynakları")
# yonetici.bilgileriGoster()
#yonetici.zamYap(1245)
# yonetici.bilgileriGoster()


""" ***********************************************************

override (iptal etme): miras alınan bir metot aynı isimle alttaki sınıfta tekrar tanımlanırsa,
metot tekrar çağrıldığında miras alınan değil, yeni oluşturulan metot çalışır. Buna override etmek denir.

**************************************************"""


class Calisan2():
    def __init__(self, isim="Bilgi Yok!", maas="Bilgi Yok!", departman="Bilgi Yok!"):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):
        print("\n...Çalışan sınıfının bilgileri...")
        print("İsim: {}\nMaaş: {}\nDepartman: {}\n".format(
            self.isim, self.maas, self.departman))

    def departmanDegistir(self, yeniDepartman):
        self.departman = yeniDepartman


class Yonetici2(Calisan2):
    def __init__(self, isim="Bilgi Yok!!", maas="Bilgi Yok!!", departman="Bilgi Yok!!", kisiSayisi="Bilgi Yok!!"):
        # override etme işlemi budur.
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisiSayisi = kisiSayisi

    def bilgileriGoster(self):
        print("\n...Yönetici sınıfının bilgileri...")
        print("İsim: {}\nMaaş: {}\nDepartman: {}\nSorumlu olduğu kişi sayısı: {}\n".format(
            self.isim, self.maas, self.departman, self.kisiSayisi))

    def zamYap(self, zamMiktarı):
        print("Zam yapılıyor...")
        self.maas += zamMiktarı


#yonetici2 = Yonetici2("Ahmet Malik Güler", 12000, "Pazarlama", 150)
# yonetici2.bilgileriGoster()

"""***********************************************

super: override ettiğimiz bir metot içinde miras aldığımız bir metodu kullanmak istersek super anahtar kelimesini 
kullanabiliriz. Yani genel anlamıyla miras aldığımız sınıfın metotlarını alt sınıflarda da kullanmamızı sağlar. yani üstteki sınıfın
init() fonksiyonunu da kullanabiliriz.

***********************************************"""


class Calisan3():
    def __init__(self, isim="Bilgi Yok!", maas="Bilgi Yok!", departman="Bilgi Yok!"):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):
        print("\n...Çalışan sınıfının bilgileri...")
        print("İsim: {}\nMaaş: {}\nDepartman: {}\n".format(
            self.isim, self.maas, self.departman))

    def departmanDegistir(self, yeniDepartman):
        self.departman = yeniDepartman


class Yonetici3(Calisan3):
    def __init__(self, isim="Bilgi Yok!!", maas="Bilgi Yok!!", departman="Bilgi Yok!!", kisiSayisi="Bilgi Yok!!"):
        super().__init__(isim, maas, departman) # bu bilgiler bir üstteki sınıftan gelir
        print("Yönetici sınıfının init fonksiyonu")
        self.kisiSayisi = kisiSayisi

    def bilgileriGoster(self):
        print("\n...Yönetici sınıfının bilgileri...")
        print("İsim: {}\nMaaş: {}\nDepartman: {}\nSorumlu olduğu kişi sayısı: {}\n".format(
            self.isim, self.maas, self.departman, self.kisiSayisi))

    def zamYap(self, zamMiktarı):
        print("Zam yapılıyor...")
        self.maas += zamMiktarı

yonetici3 = Yonetici3("Elif İkra Güler", 13000, "Pazarlama", 200)
yonetici3.bilgileriGoster()