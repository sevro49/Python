"""Kullanıcıdan aldığınız bir sayının armstrong sayısı olup olmadığını bulmaya çalışın
1634 = 1^4 + 6^4 + 3^4 + 4^4
371 = 3^3 + 7^3 + 1^3"""

while True:
    sayi = input(
        "Armstrong sayısı olup olmadığını kontrol etmek istediğiniz bir sayı giriniz (Çıkmak için 'q'): ")
    basamak = len(sayi)
    toplam = 0
    sayi2 = 0
    i = 1
    j = 10
    if(sayi == 'q'):
        print("Programdan çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        sayi2 = sayi 
        toplam += ((sayi % 10) ** basamak)
        while (basamak > i):
            sayi = sayi // j
            toplam += ((sayi % 10) ** basamak)
            i += 1
        if(toplam == sayi2):
            print("{} bir amrstrong sayıdır.".format(sayi2))
        else:
            print("{} bir amrstrong sayı değildir.".format(sayi2))
            