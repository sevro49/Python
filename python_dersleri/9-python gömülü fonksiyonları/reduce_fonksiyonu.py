"""
reduce(fonksiyon, iterasyon yapılabilen veri tipi(liste vb.))
reduce fonksiyonu, değer olarak aldığı fonksiyonu soldan başlayarak listenin ilk 2 elemanına uygular ve 
çıkan sonucu listenin 3. elemanına uygular. Bu şekilde devam ederek liste bitince bir tane değer döner.
"""
from functools import reduce

print(reduce (lambda x,y : x + y, [1,2,3,4,5]))
print(reduce (lambda x,y : x * y, [1,2,3,4,5]))

def maks(x,y):
    if x > y:
        return x
    else:
        return y

print(reduce(maks, [1,-1,35,49,30,0]))