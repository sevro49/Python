def fonksiyon(*args): #istediğimiz kadar argüman gönderebiliriz.
    for i in args:
        print(i)

fonksiyon(1,2,3)

fonksiyon(1,2,3,4,5,5,6)

def fonksiyon(isim, *args):
    print("İsim:", isim)
    print("--------")
    for i in args:
        print(i)

fonksiyon("Zeynep",12,3,4,5,5,6,6,7,)


def fonksiyon (**kwargs): #keyword args
    print(kwargs)

fonksiyon(isim = "Zeynep", soyisim = "Atar", numara = 12345)

def fonksiyon (**kwargs): 
    for i,j in kwargs.items():
        print("Argüman ismi:",i,"Argüman değeri:",j)

fonksiyon(isim = "Zeynep", soyisim = "Atar", numara = 12345)

def fonksiyon(*args, **kwargs):
    for i in args:
        print(i)

    print("----------")

    for i,j in kwargs.items():
        print(i,j)

fonksiyon(1,2,3,4,5,6,isim = "Zeynep", soyisim = "Atar", numara = 12345)


"""İç içe fonksiyon tanımlama"""

def selamlar(isim):
    print("Selam", isim)

selamlar("Zeynep")

merhaba = selamlar

del selamlar

merhaba("Emre")


def fonksiyon():
    def fonksiyon2():
        print("Küçük fonksiyondan herkese merhaba")

    fonksiyon2()
    print("Büyük fonksiyondan herkese merhaba")

fonksiyon()
# fonksiyon2() # lokal bir değer olduğu için dışarıdan erişilemez.

def fonksiyon(*args):
    def toplama(args):
        toplam = 0
        for i in args:
            toplam += i

        return toplam
    print(toplama(args))

fonksiyon(1,2,3,4,5)