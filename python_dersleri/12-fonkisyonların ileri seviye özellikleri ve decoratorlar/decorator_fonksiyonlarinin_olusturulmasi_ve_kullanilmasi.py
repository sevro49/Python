"""
Decorator fonksiyonlar, fonksiyonlarımıza dinamik olarak ekstra özellik eklediğimiz
fonksiyonlardır ve decorator kullanımı kod tekrarı yapmamızı engeller. Flask gibi
frameworklerde oldukça fazla kullanılır.
"""

import time

def kareAl(sayilar):
    sonuc = list()
    baslama = time.time()
    for i in sayilar:
        sonuc.append(i ** 2)
    bitis = time.time()
    print("Bu fonksiyon " , str(bitis - baslama) ," saniye sürdü")
    return sonuc

def kupAl(sayilar):
    sonuc = list()
    baslama = time.time()
    for i in sayilar:
        sonuc.append(i ** 3)
    bitis = time.time()
    print("Bu fonksiyon " , str(bitis - baslama) ," saniye sürdü")
    return sonuc

print(kareAl(range(100000)))
print(kupAl(range(100000)))


def zamanHesapla(func):
    def wrapper(sayilar): #decorator olması için yazmalıyız
        baslama = time.time()

        sonuc = func(sayilar)

        bitis = time.time()

        print(func.__name__ , " " , str(bitis - baslama) , " saniye sürdü")
        return sonuc

    return wrapper

@zamanHesapla #decorate etmek istediğimiz fonksiyonun üstüne yazıyoruz
def kareAl(sayilar):
    sonuc = list()
    
    for i in sayilar:
        sonuc.append(i ** 2)
    
    
    return sonuc

@zamanHesapla
def kupAl(sayilar):
    sonuc = list()
    
    for i in sayilar:
        sonuc.append(i ** 3)
    
    
    return sonuc

print(kareAl(range(100000)))
print(kupAl(range(100000)))