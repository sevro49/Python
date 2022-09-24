import sqlite3
import time

class Kitap():
    def __init__(self, isim, yazar, yayinevi, tur, baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return "\nKitap ismi: {}\nYazar: {}\nYayınevi: {}\nTür: {}\nBaskı: {}\n".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski)



class Kutuphane():
    def __init__(self):

        self.baglantiOlustur()

    def baglantiOlustur(self):
        self.baglanti = sqlite3.connect("C:/Users/Emre Güler/Documents/SEVRO49/YAZILIM/PYTHON/vscode/python dersleri/egzersiz/sqlite/kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT, yazar TEXT, yayınevi TEXT, tür TEXT, baskı INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()        

    def baglantiyiKes(self):
        self.baglanti.close()

    def kitaplariGoster(self):
        sorgu = "SELECT * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Kütüphanede kitap bulunmuyor")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)

    def kitapSorgula(self,isim):
        sorgu = "SELECT * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)

    def kitapEkle(self,kitap):
        sorgu = "INSERT INTO kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski))
        self.baglanti.commit()

    def kitapSil(self, isim):
        sorgu = "DELETE From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def baskiYukselt(self,isim):
        sorgu = "SELECT * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if (len(kitaplar) == 0 ):
            print("Böyle bir kitap bulunmuyor")

        else:
            baski = kitaplar[0][4]
            baski += 1

            sorgu2 = "UPDATE kitaplar SET baskı = ? where isim = ?"
            self.cursor.execute(sorgu2,(baski,isim,))
            self.baglanti.commit()





        






















