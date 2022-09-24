print("""******************************* 
Atm Makinesine Hoş geldiniz.

İşlemler:

1. Bakiye sorgulama
2. Para yatırma
3. Para çekme

Programdan çıkmak için 'q' ya basın
*******************************""")

bakiye = 1000

while True:
    islem = input("İşlemi seçiniz: ")
    if(islem == 'q'):
        print("Yine bekleriz.")
        break
    elif(islem == "1"):
        print("Bakiyeniz {} TL'dir".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Miktarı giriniz: "))
        bakiye += miktar
        print("Bakiyeniz {} TL'dir".format(bakiye))
    elif(islem == "3"):
        miktar = int(input("Miktarı giriniz: "))
        if(miktar > bakiye):
            print("Yetersiz Bakiye!!")
        else:
            bakiye -= miktar
            print("Bakiyeniz {} TL'dir".format(bakiye))
