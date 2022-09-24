"""
Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;

                     1. Şarkı İsmi 
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi

                     Örnek Metodlar;

                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil
                     
"""

import sqlite3
import time
import math

class Sarki():
    def __init__(self, isim,sanatci,album,sirket,sure):
        self.isim = isim
        self.sanatci = sanatci 
        self.album = album
        self.sirket = sirket
        self.sure = sure

    def __str__(self):
        return "\nŞarkı ismi: {}\nSanatçı: {}\nAlbüm: {}\nProdüksiyon Şirketi: {}\nŞarkı süresi: {}\n".format(self.isim,self.sanatci,self.album,self.sirket,self.sure)

class Muzik():
    def __init__(self):
        self.baglantiOlustur()

    def baglantiOlustur(self):
        self.baglanti = sqlite3.connect("C:/Users/Emre Güler/Documents/SEVRO49/YAZILIM/PYTHON/vscode/python dersleri/odev/odev11 (sqlite veritabanı/müzik.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS müzik (isim TEXT, sanatçı TEXT, albüm TEXT, prodüksiyon şirketi TEXT, süre FLOAT)"

        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyiKes(self):
        self.baglanti.close()

    def sarkiEkle(self, sarki):
        sorgu = "INSERT INTO müzik Values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.sirket,sarki.sure))
        self.baglanti.commit()

    def sarkiSil(self, isim):
        sorgu = "DELETE From müzik where isim = ?"
        self.cursor.execute(sorgu, (isim,))
        self.baglanti.commit()

    def toplamSure(self):
        sorgu = "SELECT süre From müzik"
        self.cursor.execute(sorgu)
        toplamZaman = self.cursor.fetchall()

        if(len(toplamZaman) == 0):
            print("Hiç parça bulunmuyor")

        else:
            
            toplam = 0
            for i in toplamZaman:
                toplam += i[0]

            print("Toplam zaman hesaplanıyor...")
            time.sleep(2)
            print("Tüm şarkıların toplam çalma süresi: {}".format(toplam))

    def sarkiSorgulama(self, isim):
        sorgu = "SELECT * From müzik where isim = ?"
        self.cursor.execute(sorgu, (isim,))
        sarki = self.cursor.fetchall()

        if (len(sarki) == 0):
            print("Böyle bir parça bulunmuyor")

        else:
            s = Sarki(sarki[0][0],sarki[0][1],sarki[0][2],sarki[0][3],sarki[0][4])
            print(s)

    def sarkiListesi(self):
        sorgu = "SELECT * From müzik"
        self.cursor.execute(sorgu)
        liste = self.cursor.fetchall()

        if(len(liste) == 0):
            print("Hiç parça bulunmuyor")

        else:
            for i in liste:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    