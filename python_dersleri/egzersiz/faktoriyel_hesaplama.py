print("""******************************* 
Faktöriyel Bulma Programı

Çıkmak için 'q' ya basınız.
*******************************""")

while True:
    sayi = (
        input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz (çıkmak için 'q'): "))
    sonuc = 1
    if(sayi == 'q'):
        print("Güle Güle!")
        break
    else:
        sayi = int(sayi)
        print(sayi)
        for i in range(2, (sayi+1)):
            sonuc *= i
        print("{}! = {}".format(sayi, sonuc))
