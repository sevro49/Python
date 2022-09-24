"""
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulun
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya mükemmel sayı denir.
6 = 1 + 2 + 3
"""

while True:
    sayi = input("Mükemmel olup olmadığını merak ettiğiniz sayıyı giriniz (Çıkmak için 'q'): ")
    toplam = 0
    i = 1
    liste = []
    if(sayi == 'q'):
        print("Program sonlandırılıyor...")
        break
    else:
        sayi = int(sayi)
        while i != sayi:
            if(sayi % i == 0):
                toplam += i
                liste.append(i)
                
            i += 1
        if(toplam == sayi):
            print("{} mükemmel bir sayıdır.".format(sayi))
            print(liste)
        else:
            print("{} mükemmel bir sayı değildir.".format(sayi))