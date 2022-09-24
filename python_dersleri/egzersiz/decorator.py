
def ekstra (fonk):
    def wrapper(sayilar):
        ciftlerToplami = 0
        ciftler = 0
        teklerToplami = 0
        tekler = 0

        for sayi in sayilar:

            if(sayi % 2 == 0):
                ciftlerToplami += sayi
                ciftler += 1

            else:
                teklerToplami += sayi
                tekler += 1

        print("Teklerin ortalaması:",teklerToplami / tekler)
        print("Çiftlerin ortalaması:",ciftlerToplami / ciftler)

        fonk(sayilar)

    return wrapper
        



@ekstra
def ortalamaBul(sayilar):

    toplam = 0

    for i in sayilar:
        toplam += i

    print("Genel ortalama:",toplam / len(sayilar))

ortalamaBul([1,2,3,4,5,6,7,8,9,10])