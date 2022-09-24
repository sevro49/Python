class Takim():
    def __init__(self, ad="Bilgi Yok!", sehir="Bilgi Yok!", sampiyonlukSayısı="Bilgi Yok!", guncelSıralama="Bilgi Yok!"):
        print("init fonksiyonu çağrıldı")
        self.ad = ad
        self.sehir = sehir
        self.sampiyonlukSayısı = sampiyonlukSayısı
        self.guncelSıralama = guncelSıralama


galatasaray = Takim("Galatasaray", "İstanbul", 22, 15)
fenerbahce = Takim("Fenerbahçe", "İstanbul", 19, 5)
besiktas = Takim("Beşiktaş", "İstanbul", 16, 6)
trabzonspor = Takim("Trabzonspor", "Trabzon", 7, 1)
goztepe = Takim("Göztepe", "İzmir", 0, 14)
antalyaspor = Takim("Antalyaspor", "Antalya", 0)

print(galatasaray.ad)
print(galatasaray.guncelSıralama)
print(fenerbahce.sampiyonlukSayısı)
print(trabzonspor.guncelSıralama)
print(antalyaspor.sehir)
print(antalyaspor.guncelSıralama)