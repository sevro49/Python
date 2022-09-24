"""Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın."""

toplam = 0
while True:
    sayi = input("Toplamak istediğiniz sayıyı girin (Çıkmak için 'q'): ")
    if(sayi == 'q'):
        print("Toplam =",toplam)
        print("Program Sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)
        toplam += sayi
    