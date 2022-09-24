"""Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve 
sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]"""

def ucgenMi(a):
    if(a[0]-a[2] < a[1] < a[0]+a[2]):
        return a




liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(ucgenMi, liste)))