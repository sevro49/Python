def selamla(isim):
    print("Merhaba...", isim)
    print("Nasılsınız")

selamla("Emre")

def toplama(a,b,c):
    print("Toplam =",a+b+c)

toplama(10,20,30)

def faktoriyel(sayi):
    faktoriyel = 1
    if(sayi == 0 or sayi == 1):
        print("Faktöriyel:",faktoriyel)
    else:
        while sayi >= 1:
            faktoriyel *= sayi
            sayi -= 1
        print("Faktöriyel:",faktoriyel)

faktoriyel(1)
faktoriyel(0)
faktoriyel(2)
faktoriyel(3)