class Yazilimci():
    def __init__(self, isim, soyisim, maas, numara, diller):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.numara = numara
        self.diller = diller

    def bilgileriGoster(self):
        print("""
        Yazılımcı objesinin özellikleri
        
        İsim: {}
        Soyisim: {}
        Numara: {}
        Maaş: {}
        Bildiği diller: {}
        """.format(self.isim, self.soyisim, self.numara, self.maas, self.diller))

    def zamYap(self, zamMiktari):
        print("Zam yapılıyor...")
        self.maas += zamMiktari

    def dilEkle(self, yeniDil):
        print("Dil ekleniyor...")
        self.diller.append(yeniDil)

    def numaraDegistirme(self, yeniNumara):
        print("Numara değiştiriliyor...")
        self.numara = yeniNumara

    


yazilimci1 = Yazilimci("Emre", "Güler", 12345, 10000, ["Python", "Java", "C"])
yazilimci1.bilgileriGoster()
yazilimci1.dilEkle("JS")
yazilimci1.zamYap(1500)
yazilimci1.bilgileriGoster()
yazilimci1.numaraDegistirme(53654448866)
yazilimci1.bilgileriGoster()
