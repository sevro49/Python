"""
çoğu metot biz tanımlamasak da python tarafından tanımlıdır. Bazı metotları bizim tanımlamamız gerekir.
kitap1 = Kitap() # __init__ metodu çağrılıyor
len(kitap1) # __len__ metodu çağrılacak ama tanımlı değil. Bu metodu tanımlamalıyız.

"""

"""class Kitap():
    pass

kitap1 = Kitap() ## __init__ metodu
print(kitap1) ## __str__ metodu
len(kitap1) ## __len__ metodu
del kitap1 ## __del__ motodu """

class Kitap():
    def __init__(self, isim, yazar, sayfaSayisi, tur):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfaSayisi = sayfaSayisi
        self.tur = tur

kitap = Kitap("İstanbul Hatırası", "Ahmet Ümit", 561, "Polisiye")
print(kitap)

class Kitap2():
    def __init__(self, isim, yazar, sayfaSayisi, tur):
        print("init fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfaSayisi = sayfaSayisi
        self.tur = tur
    
    def __str__(self): #print(objeAdi) yazarak ulaşılabilir
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTür: {}\n".format(self.isim,self.yazar,self.sayfaSayisi,self.tur)

    def __len__(self):
        return self.sayfaSayisi

    def __del__(self):
        print("Kitap objesi siliniyor...")

kitap2 = Kitap2("İstanbul Hatırası", "Ahmet Ümit", 561, "Polisiye")
print(kitap2)
print(len(kitap2))
del kitap2
print(kitap2)
