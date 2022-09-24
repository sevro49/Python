"""Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın."""


def ebob(a, b):
    i = 1
    ebob = 1

    while (i <= a and i <= b):
        if(not (a % i) and not (b % i)):
            ebob = i
        i += 1
        
    return ebob

sayi1 = int(input("Sayı 1 = "))
sayi2 = int(input("Sayı 2 = "))

print("EBOB = ",ebob(sayi1,sayi2))