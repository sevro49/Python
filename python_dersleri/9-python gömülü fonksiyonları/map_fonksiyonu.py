"""
map() fonksiyonu ilk paramterle olarak bir tane fonksiyon objesi alır. 
2.parametre olarak da bir tane iterasyon yapacak veritipi alarak gönderilen fonksiyonu her bir eleman üzerinde 
uygulayarak sonuçları map objesi olarak döner.

map(fonksiyon, iterasyon yapılabikecek veritipi(liste, demet vb.)....)
"""


def double(x):
    return x * 2

# map(double, [1,2,3,4,5,6,7]) #her bir elemana double fonksiyonunu uyguluyoruz.
print(list(map(double, [1,2,3,4,5,6,7])))

print(list(map(lambda x : x ** 2,(1,2,3,4,5,6,7,8,9,10)))) # lambda ile fonksiyon tanımlama.

liste1 = [1,2,3,4]
liste2 = [5,6,7,8]
liste3 = [9,10,11,12,13]

print(list(map(lambda x,y : x*y, liste1, liste2)))