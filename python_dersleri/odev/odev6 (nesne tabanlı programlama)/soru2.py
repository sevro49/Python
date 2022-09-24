"""
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
"""

import time

class Bilgisayar():
    def __init__(self, pcDurum = "Kapalı", pcMarka = "Monster", pcYas = 2, acikUygulama = "Hiçbir uygulama çalışmıor."):
        self.pcDurum = pcDurum
        self.pcMarka = pcMarka
        self.pcYas = pcYas
        self.acikUygulama = acikUygulama
    
    def pcAc(self):
        if(self.pcDurum == "Açık"):
            print("Bilgisayarınız zaten açık...")
        else:
            print("Bilgisayarınız açılıyor...")
            self.pcDurum = "Açık"
            time.sleep(1)
            print("Bilgisayarınız açıldı...")

    def pcKapa(self):
        if(self.pcDurum == "Kapalı"):
            print("Bilgisayarınız zaten kapalı...")

        else:
            print("Bilgisayarınız kapanıyor...")
            self.pcDurum = "Kapalı"
            time.sleep(1)
            print("Bilgisayarınız kapandı...")

    def uygulamaAc(self, uygulamaAdi):
        print("{} açılıyor".format(uygulamaAdi))
        time.sleep(1)
        self.acikUygulama = uygulamaAdi
        print("{} açıldı".format(uygulamaAdi))

    def uygulamaKapat(self,):
        print("{} kapatılıyor...".format(self.acikUygulama))
        time.sleep(1)
        self.acikUygulama = "Hiçbir uygulama çalışmıyor..."
        print("{} kapatıldı...".format(self.acikUygulama))

pc = Bilgisayar()

while True:
    print("""
    ********************* 
    Bilgisayar
    
    Yapmak istediğiniz işlemi seçiniz: 
    
    1. Bilgisayarı aç
    2. Bilgisayarı kapat
    3. Uygulama aç
    4. Uygulama kapat

    Çıkmak için 'q' ya basın.
    *********************""")

    secim = input("işlemi seçiniz: ")

    if(secim == 'q'):
        print("Bilgisayar kapanıyor...")
        break

    elif(secim == '1'):
        pc.pcAc()

    elif(secim == '2'):
        pc.pcKapa()

    elif(secim == '3'):
        uygulama = input("Açmak istediğiniz uygulama adını girin: ")
        pc.uygulamaAc(uygulama)
    
    elif(secim == '4'):
        pc.uygulamaKapat()

        


    