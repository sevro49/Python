"""Kodlama Egzersizimizde yazdığımız Kumanda Sınıfına ek olarak metodlar ve özellikler eklemeye çalışın."""

import random
import time
from tkinter import TkVersion


class Kumanda():

    def __init__(self, tvDurum="Kapalı", tvSes=0, kanalListesi=["Trt"], kanal="Trt", favoriKanallar = ["Trt"]):
        self.tvDurum = tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal
        self.favoriKanallar = favoriKanallar

    def tvAc(self):
        if(self.tvDurum == "Açık"):
            print("Televizyon zaten açık...")

        else:
            print("Televizyon açılıyor")
            self.tvDurum = "Açık"

    def tvKapat(self):
        if(self.tvDurum == "Kapalı"):
            print("Televizyon zaten kapalı")

        else:
            print("Televizyon kapanıyor...")
            self.tvDurum = "Kapalı"

    def sesAyarlari(self):
        while True:
            cevap = input("Sesi azalt: '<'\nSesi arttır: '>'\nÇıkış : çıkış ")

            if(cevap == '<'):
                if(self.tvSes != 0):
                    self.tvSes -= 1
                    print("Ses:", self.tvSes)
            elif(cevap == '>'):
                if(self.tvSes != 31):
                    self.tvSes += 1
                    print("Ses:", self.tvSes)
            else:
                print("Ses güncellendi:", self.tvSes)
                break

    def kanalEkle(self, kanalIsmı):
        print("Kanal ekleniyor...")
        time.sleep(1)  # program 1 saniye uyur.
        self.kanalListesi.append(kanalIsmı)
        print("Kanal eklendi...")

    def kanalSil(self, kanalIsmi):
        print("Kanal siliniyor...")
        time.sleep(1)
        self.kanalListesi.remove(kanalIsmi)
        print("Kanal silindi...")

    def rastgeleKanal(self):
        rastgele = random.randint(0, len(self.kanalListesi)-1)
        self.kanal = self.kanalListesi[rastgele]
        print("Şu anki kanal:", self.kanal)

    def favoriKanalEkleme(self, kanalIsmi):
        print("Favori kanal ekleniyor...")
        time.sleep(1)
        self.favoriKanallar.append(kanalIsmi)
        print("istediğiniz kanal favori kanallar listesine eklendi...")

    def favoriListesi(self):
        print("Favori kanal listesi:")
        return self.favoriKanallar
        
        

    def __len__(self):
        return len(self.kanalListesi)

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n".format(self.tvDurum, self.tvSes, self.kanalListesi, self.kanal)


kumanda = Kumanda()

while True:

    print("""
    *********************** 
    Televizyon Uygulaması

    1. Tv Aç
    2. Tv Kapat
    3. Ses Ayarları
    4. Kanal ekle
    5. Kanal sil
    6. Kanal Sayısını Öğrenme
    7. Favori listeme ekle
    8. Favori listemi göster
    9. Rastgele Kanala Geçme
    10. Televizyon bilgileri

    Çıkmak için 'q' ya basın.
    ***********************""")

    islem = input("İşlemi seçiniz: ")

    if(islem == 'q'):
        print("Program sonlandırılıyor...")
        break

    elif(islem == '1'):
        kumanda.tvAc()

    elif(islem == '2'):
        kumanda.tvKapat()

    elif(islem == '3'):
        kumanda.sesAyarlari()

    elif(islem == '4'):
        kanalIsimleri = input("Eklemek istediğimiz kanal isimlerini ',' ile ayırarak girin: ")
        # ',' ile elamanları ayırmaya yarar
        kanalListesi = kanalIsimleri.split(",")
        for eklenecekler in kanalListesi:
            kumanda.kanalEkle(eklenecekler)
    
    elif(islem == '5'):
        kanalIsımleri = input("Silmek istediğiniz kanal isimlerini ',' ile ayırarak girin: ")
        kanalListesi = kanalIsımleri.split(",")
        for silinecekler in kanalListesi:
            kumanda.kanalSil(silinecekler)

    elif(islem == '6'):
        print("Kanal sayısı:",len(kumanda))

    elif(islem == '7'):
        kanalIsimleri = input("Favorilerinize eklemek istediğiniz kanal isimlerini ',' ile ayırarak girin: ")
        kanalListesi = kanalIsimleri.split(",")
        for favori in kanalListesi:
            kumanda.favoriKanallar.append(favori)

    elif(islem == '8'):
        kumanda.favoriListesi()
        
    elif(islem == '9'):
        kumanda.rastgeleKanal()

    elif(islem == '10'):
        print(kumanda)

    else:
        print("Geçersiz işlem!!!")
