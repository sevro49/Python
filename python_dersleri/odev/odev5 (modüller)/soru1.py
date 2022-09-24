"""Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın."""

from modul_emre import *


while True:

    print("""
    **************** 

    Fonksiyonel Hesap Makinesi

    Yapmak istediğiniz işlemi seçin:
    1. Faktöriyel hesaplama
    2. Bir sonraki sayıya yuvarlama
    3. Bir önceki sayıya yuvarlama

    ****************""")

    secim = int(input("İşlem (çıkmak için '-1'): "))

    if(secim == -1):
        print("Program sonlandırılıyor...")
        break
    elif (secim == 1):
        while True:
            sayi = int(input(
                "Faktöriyelini hesaplamak istediğiniz sayıyı girin (geri gelmek için '-1'): "))
            if(sayi == -1):
                break
            else:
                faktoriyel(sayi)
    elif(secim == 2):
        while True:
            sayi = float(
                input("Bir üste yuvarlamak istediğiniz sayıyıyı giriniz (geri gelmek için '-1'): "))
            if(sayi == -1):
                break
            else:
                ceil(sayi)
    elif(secim == 3):
        while True:
            sayi = float(
                input("Bir alta yuvarlamak istediğiniz sayıyıyı giriniz (geri gelmek için '-1'): "))
            if(sayi == -1):
                break
            else:
                floor(sayi)
