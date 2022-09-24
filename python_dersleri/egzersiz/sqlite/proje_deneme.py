from kutuphane import *

print("""
**********************
Kütüphane programına hoş geldiniz

İşlemler:

1. Kitapları Göster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt

Çıkmak için 'q' ya basın.
**********************
""")

kutuphane = Kutuphane()

while True:
    islem = input("Yapacağınız işlem: ")

    if(islem == 'q'):
        print("Program sonlandırılıyor...")
        print("yine bekleriz...")
        break

    elif (islem == "1"):
        kutuphane.kitaplariGoster()

    elif (islem == "2"):
        isim = input("Hangi kitabı istiyorsunuz? ")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        kutuphane.kitapSorgula(isim)

    elif (islem == "3"):
        isim = input("Eklemek istediğiniz kitabın adını giriniz: ")
        yazar = input("Eklemek istediğiniz kitabın yazarının adını giriniz: ")
        yayinevi = input("Eklemek istediğiniz kitabın yayınevini giriniz: ")
        tur = input("Eklemek istediğiniz kitabın türünü giriniz: ")
        baski = int(input("Eklemek istediğiniz kitabın baskısını giriniz: "))
        yeniKitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kutuphane.kitapEkle(yeniKitap)
        print("Kitap eklendi...")

    elif (islem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ?")
        cevap = input("Emin misiniz? (E/H): ")
        if (cevap.upper() == "E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitapSil(isim)
            print("Kitap silindi")
        
    elif (islem == "5"):
        isim = input("Hangi kitabın baskını yükseltmek istiyorsunuz? ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        print("Baskı yükseltildi...")
        kutuphane.baskiYukselt(isim)

    else:
        print("Geçersiz işlem!!!")