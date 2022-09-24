"""
filter,
reduce fonksiyonu ile birebir aynıdır. tek farkı girilen fonksiyon true ya da false döner

filter(fonksiyon, iterasyon yapabilen bir veri tipi(liste vb.))
"""
print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8]))) 