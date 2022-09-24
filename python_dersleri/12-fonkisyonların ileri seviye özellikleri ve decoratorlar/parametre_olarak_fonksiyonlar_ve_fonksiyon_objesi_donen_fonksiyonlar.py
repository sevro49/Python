from itertools import combinations_with_replacement


def anaFonksiyon (islemAdi):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islemAdi == "toplama":
        return toplama

    else:
        return carpim

fonk = anaFonksiyon("toplama")
print(fonk(1,2,3,4,5))

fonk2 = anaFonksiyon("carpim")
print(fonk2(1,2,3,4,5))


"""fonksiyonları argüman olarak göndermek"""

def toplama(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def carpma (a,b):
    return a*b

def bolme (a,b):
    return a / b

def anaFonksiyon (func1, func2, func3, func4, islemAdi):

    if (islemAdi == "toplama"):
        print(func1(3,4))

    elif (islemAdi == "cikarma"):
        print(func2(16,5))

    elif (islemAdi == "carpma"):
        print(func3(3,5))
    
    elif (islemAdi == "bolme"):
        print(func4(10,2))

    else:
        print("Geçersiz işlem")

anaFonksiyon(toplama, cikarma, carpma, bolme, "bolme")