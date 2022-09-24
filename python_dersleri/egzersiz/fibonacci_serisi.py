print("""********************* 
Fibonacci serisi oluşturan program
1,1,2,3,5,8,13,21,34....

Hesaplamak istediğiniz fibonacci serisi adım sayısını giriniz
Çıkmak için 'q'
*********************""")

while True:
    adim = input("Adım sayısını giriniz (Çıkmak için 'q'): ")
    seri = [1, 1]
    i = 0
    j = 1
    if(adim == 'q'):
        print("Program sonlandırıldı...")
        break
    else:
        adim = int(adim)
        while ((adim-2) > 0):
            seri.append(seri[i] + seri[j])
            i += 1
            j += 1
            adim -= 1
        print(seri)
