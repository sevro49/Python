from soru2 import *

print("""
******************* 
Müzik Programına Hoş Geldiniz!!

İşlemler:
1. Şarkı Ekleme
2. Şarkı Silme
3. Şarkıların toplam süresini görme
4. Şarkı sorgulama
5. Şarkı Listesi

Çıkmak için 'q'ya basın

*******************""")



muzik = Muzik()

while True:

    islem = input("Yapmak istediğiniz işlemi seçin: ")

    if (islem == 'q'):
        print("Program sonlandırılıyor...")
        time.sleep(1)
        print("Program sonlandı...")
        break

    elif (islem == '1'):
        isim = input("Eklemek istediğiniz şarkının adı: ")
        sanatci = input("Eklemek istediğiniz şarkının sanatçısı: ")
        album = input("Eklemek istediğiniz şarkını albümü: ")
        sirket = input("Eklemek istediğiniz şarkının prodüksiyon şirketi: ")
        sure = input("Eklemek istediğiniz şarkının süresi: ")

        yeniSarki = Sarki(isim,sanatci,album,sirket,sure)
        print("Şarkı ekleniyor...")
        time.sleep(2)
        muzik.sarkiEkle(yeniSarki)
        print("Şarkı eklendi...")
        
    elif (islem == '2'):
        isim = input("Hangi şarkıyı silmek istiyorsunuz? ")
        print("Şarkı siliniyor...")
        time.sleep(2)
        muzik.sarkiSil(isim)
        print("Şarkı silindi...")

    elif (islem == '3'):
        muzik.toplamSure()

    elif (islem == '4'):
        isim = input("Sorgulamak istediğiniz şarkının adı: ")
        print("Şarkı sorgulanıyor...")
        time.sleep(2)
        muzik.sarkiSorgulama(isim)

    elif (islem == '5'):
        muzik.sarkiListesi()










