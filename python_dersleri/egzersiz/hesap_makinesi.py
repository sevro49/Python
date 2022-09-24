print("""**********************

Hesap Makinesi Programı

İşlemler:
1. Toplama işlemi
2. Çıkarma işlemi
3. Çarpma işlemi
4. Bölme işlemi

**********************
""")

a = int(input("1. sayı: "))
b = int(input("2. sayı: "))

islem = input("İşlemi giriniz: ")

if islem == "1":
    print("{} ile {}'nın toplamı {}'dır.".format(a,b,a+b))
elif islem == "2":
    print("{} ile {}'nın farkı {}'dır.".format(a,b,a-b))
elif islem == "3":
    print("{} ile {}'nın çarpımı {}'dır.".format(a,b,a*b))
elif islem == "4":
    print("{} ile {}'nın bölümü {}'dır.".format(a,b,a/b))
else:
    print("Geçersiz işlem!!")