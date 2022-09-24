def selamla(isim):
    print("Selam,", isim)


selamla("Emre")


def selamlar(isim="İsimsiz"):
    print("Selamlar", isim)


selamlar()  # fonksiyon içine bir değer vermezsek varsayılan değerini girer.
selamlar("Emre")  # içine bir değer verirsek varsayılan değerle çakışmaz.

def bilgileriGoster (ad = "Bilgi Yok", soyad = "Bilgi Yok", numara = "Bilgi Yok"):
    print("Ad:", ad, "Soyad:",soyad ,"Numara:", numara)

bilgileriGoster("Emre", "12345") # bu şekilde yaparsak sıralı girmek zorunda kalırız. soyad: 12345 olur
bilgileriGoster(numara = "12345", ad = "Emre") # bu şekilde yaparsak sıralı girmemiş oluruz.

def toplama (a,b,c):
    print(a+b+c)

toplama(3,4,5)
#toplama(3,4,5,6) # normal şartlar altında 3 parametresi olan bir fonksiyona 4 değer giremeyiz

def toplam(*a):
    print(a)

toplam(1,2,3,4) #  *a ile tanımladığımız için istediğimiz kadar değer girebiliyoruz.
toplam(1,2)

def toplam2(*a):    # metot içine for döngüsü yazarak toplama işlemi yapabiliriz.
    toplam = 0
    for i in a:
        toplam += i
    print(toplam)

toplam2(1,2,3,4,5)
